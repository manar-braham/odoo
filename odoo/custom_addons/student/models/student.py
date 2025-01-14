from odoo import api, fields, models



class Student(models.Model):
    _name = "wb.student"
    _description = "This is school profile."

    name = fields.Char("Name")
    name1 = fields.Char("Name1")
    name2 = fields.Char("Name2")
    name3 = fields.Char("Name3")
    name4 = fields.Char("Name4")