from odoo import models, fields, api

class Keyholder(models.Model.):
    _name = 'latihan_memalak.Keyholder'
    _description = 'latihan_memalak.keyholder'
    
    
    oknum_id = fields.Many2one('latihan_memalak.oknum', string="Nama")
    bagian_persen = fields.Char(string="Bagian Persen")
    jumlah_bagian = fields.Float(string="Bagian yang didapatkan", compute="_compute_bagian")

    project_id = fields.Many2one('project.project', string="Project")
    
    @api.depends('bagian_peresen')
    def _compute_bagian(self):
        for record in self:
            record.jumlah_bagian = record.bagian_persen + record.project_id.backdoor_salary / 100