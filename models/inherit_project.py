from odoo import models, fields, api

class pembagian_persenan(models.Model):
    _inherit = 'project.project'
    
    anggaran = fields.Float(string="Anggaran")
    persenan = fields.Float(string="Persenan")
    backdoor_salary = fields.Float(string="Gaji Sepihak", compute="_compute_gaji_sepihak")
    
    keyholder_ids = fields.One2many('latihan_memalak.keyholder', 'project_id', string="Keyholder")
    
    
    @api.depends('pesenan', 'anggaran')
    def _compute_gaji_sepihak(self):
        for record in self:
            record.backdoor_salary = record.persenan * record.anggaran / 100