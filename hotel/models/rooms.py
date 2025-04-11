# -*- coding: utf-8 -*-
# rooms.py

from odoo import models, fields, api

class rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'Hotel Rooms'

    name = fields.Char("Room No.")
    description = fields.Char("Room Description")
