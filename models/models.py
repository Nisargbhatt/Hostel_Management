# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hostel_managment(models.Model):
     _name = 'hostel_managment.student'
     _rec_name="name"
     image = fields.Binary(attachment=True)

     name = fields.Char(string="student name", required=True)

     lastname = fields.Char(string="Last Name")

     middlename = fields.Char(string="Father Name")

     dob = fields.Date(string="Date of Birth")

     blood_group = fields.Selection(
         [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
          ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
         'Blood Group')

     s_no = fields.Char("Enrollment no", constraint='primary')

     s_gender = fields.Selection([
         ('male','Male'),
         ('female','Female')
     ], string="Gender", required=True, copy=False, default='male' )

     nationality = fields.Many2one('res.country', 'Nationality')

     school = fields.Selection(selection=[('gpg','Goverment Polytechnic'),('vpmp','VPMP'),('nirma','Nirma'),('rc_technical','R_C_Technical')], required=True)

     course = fields.Char("Course")

     lang = fields.Char("language")

     s_address = fields.Char(string="Student address")

     s_pincode = fields.Char(string="Pincode")

     s_contact_no = fields.Char("contact number")

     f_contact_no = fields.Char("Father's Contact number")



class student_caretaker(models.Model):
     _name = 'student.caretaker'
     _rec_name="c_name"
     image = fields.Binary(attachment=True)
     c_name = fields.Char(string="Name", required=True)
     c_contact_no = fields.Char(string="Contact Number")
     c_address = fields.Char(string="Address")


class hostel_rooms(models.Model):
     _name = 'hostel_managment.hostel_rooms'

     _rec_name="room_no"
     room_no = fields.Char("Room Number", required=True)
     room_code =  fields.Char(string="Code", required=True)
     room_faci = fields.Many2many('hostel_managment.facilities','faci_name')
     room_rent = fields.Float(String="Room Rent")
     room_capacity = fields.Integer("Room Capacity")


# Room facilities

class room_facilities(models.Model):
     _name = 'hostel_managment.facilities'

     _rec_name="faci_name"

     faci_name = fields.Char(string="Name")

     faci_quantity = fields.Float(string="Quantity")


#Room allocation

class room_allocation(models.Model):
     _name = 'hostel_managment.room_allocation'

     a_room_no = fields.Many2one('hostel_managment.hostel_rooms','room_no')

     a_students = fields.Many2many('hostel_managment.student')

     a_caretaker = fields.Many2one('student.caretaker','c_name')
