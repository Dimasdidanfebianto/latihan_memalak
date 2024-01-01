from odoo import models, api, fields, _


class UserMayotitas(models.Model):
    _name ='latihan_memalak.user_mayoritas'
    _description = 'latihan_memalak.user_mayoritas'
    
    name = fields.Char(string="Nama")
    jabatan = fields.Char(string="Jabatan")
    domisili = fields.Char(string="Domisili")
    
    