#!/usr/bin/env python3

"""
 ****************************************************************************
 Filename:          maintenance.py
 Description:       maintenance REST Api

 Creation Date:     02/11/2020
 Author:            Ajay Paratmandali

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 ****************************************************************************
"""

from .view import CsmView, CsmAuth
from eos.utils.log import Log
from csm.common.errors import InvalidRequest
from csm.core.blogic import const
from csm.core.controllers.validators import Enum, ValidationErrorFormatter
from marshmallow import (Schema, fields, ValidationError)
from csm.common.permission_names import Resource, Action


class GetMaintenanceSchema(Schema):
    action = fields.Str(required=True, validate=[Enum(["node_status"])])

class PostMaintenanceSchema(Schema):
    action_items = [const.SHUTDOWN, const.START, const.STOP]
    resource_name = fields.Str(required=True)
    action = fields.Str(required=True, validate=[Enum(action_items)])

@CsmView._app_routes.view("/api/v1/maintenance/cluster/{action}")
class MaintenanceView(CsmView):
    def __init__(self, request):
        super(MaintenanceView, self).__init__(request)
        self._service = self.request.app[const.MAINTENANCE_SERVICE]

    @CsmAuth.permissions({Resource.SYSTEM: {Action.LIST}})
    async def get(self):
        """
        Fetch All the Node Current Status.
        """
        Log.debug("Handling maintenance request")
        action = self.request.match_info[const.ACTION]
        try:
            GetMaintenanceSchema().load({const.ACTION: action},
                                        unknown=const.const.MARSHMALLOW_EXCLUDE)
        except ValidationError as e:
            raise InvalidRequest(f"{ValidationErrorFormatter.format(e)}")
        return await self._service.get_status()

    @CsmAuth.permissions({Resource.SYSTEM: {Action.UPDATE}})
    async def post(self):
        """
        Process Service Requests for Cluster Shutdown or Node Start Stop.
        :return:
        """
        Log.debug("Handling maintenance request")
        action = self.request.match_info[const.ACTION]
        body = await self.request.json()
        body[const.ACTION] = action
        try:
            PostMaintenanceSchema().load(body,
                                         unknown=const.MARSHMALLOW_EXCLUDE)
        except ValidationError as e:
            raise InvalidRequest(f"{ValidationErrorFormatter.format(e)}")
        service_action = {
            const.SHUTDOWN: self._service.shutdown,
            const.START: self._service.start,
            const.STOP: self._service.stop
        }
        return await service_action[action](**body)
