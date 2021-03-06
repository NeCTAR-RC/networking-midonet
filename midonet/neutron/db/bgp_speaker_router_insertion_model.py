# Copyright (C) 2016 Midokura SARL
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sqlalchemy as sa

from neutron_lib.db import model_base


class BgpSpeakerRouterAssociation(model_base.BASEV2):

    """Tracks Bgp Speaker Router Association"""

    __tablename__ = 'bgp_speaker_router_associations'

    bgp_speaker_id = sa.Column(
        sa.String(36),
        sa.ForeignKey('bgp_speakers.id', ondelete="CASCADE"),
        nullable=False, primary_key=True)
    router_id = sa.Column(
        sa.String(36),
        sa.ForeignKey('routers.id', ondelete="CASCADE"),
        nullable=False, unique=True)
