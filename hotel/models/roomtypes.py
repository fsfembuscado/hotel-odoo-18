# -*- coding: utf-8 -*-
# roomtypes.py

from odoo import models, fields, api

class roomTypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Types Master List'

    name = fields.Char("Room Type", required=True)
    description = fields.Char("Room Type Description")
    
    room_image = fields.Image("Room Image")
    bathroom_image = fields.Image("Bathroom Image")
    
    daily_charges = fields.Float("Daily Charges")