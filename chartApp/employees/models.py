# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AtsUtilization(models.Model):
    pmt = models.CharField(max_length=200, blank=True, null=True)
    attuid = models.CharField(max_length=10, blank=True, null=True)
    employeename = models.CharField(max_length=200, blank=True, null=True)
    jobtitle = models.CharField(max_length=200, blank=True, null=True)
    supervisor = models.CharField(max_length=200, blank=True, null=True)
    workname = models.CharField(max_length=200, blank=True, null=True)
    worktype = models.CharField(max_length=200, blank=True, null=True)
    emptype = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    pvdate = models.CharField(max_length=30, blank=True, null=True)
    billedhrs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ats_utilization'


class AttCalendar(models.Model):
    year = models.CharField(max_length=13, blank=True, null=True)
    month = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    attcapacity = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    idccapacity = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_calendar'


class IdcProjectSystemTools(models.Model):
    team = models.CharField(max_length=4000, blank=True, null=True)
    project = models.CharField(max_length=4000, blank=True, null=True)
    system = models.CharField(max_length=4000, blank=True, null=True)
    tools = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idc_project_system_tools'


class IdcReference(models.Model):
    idcprojectname = models.CharField(max_length=100, blank=True, null=True)
    pmt = models.CharField(max_length=200, blank=True, null=True)
    workname = models.CharField(max_length=200, blank=True, null=True)
    vicepresident = models.CharField(max_length=100, blank=True, null=True)
    domain = models.CharField(max_length=100, blank=True, null=True)
    onshorecontact = models.CharField(max_length=100, blank=True, null=True)
    idccontact = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idc_reference'


class IdcUtilization(models.Model):
    pmt = models.CharField(max_length=200, blank=True, null=True)
    attuid = models.CharField(max_length=10, blank=True, null=True)
    employeename = models.CharField(max_length=200, blank=True, null=True)
    jobtitle = models.CharField(max_length=200, blank=True, null=True)
    supervisor = models.CharField(max_length=200, blank=True, null=True)
    workname = models.CharField(max_length=200, blank=True, null=True)
    worktype = models.CharField(max_length=200, blank=True, null=True)
    schedulestart = models.DateField(blank=True, null=True)
    schedulefinish = models.DateField(blank=True, null=True)
    entitytype = models.CharField(max_length=200, blank=True, null=True)
    emptype = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.CharField(max_length=200, blank=True, null=True)
    reqby = models.CharField(max_length=200, blank=True, null=True)
    team = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    pvdate = models.CharField(max_length=30, blank=True, null=True)
    billedhrs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idc_utilization'



class IDCVPHeadcountV(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vicepresident =   models.CharField(max_length=100, blank=True, null=True)        
    janheadcount = models.IntegerField()
    febheadcount = models.IntegerField()
    marheadcount = models.IntegerField()
    aprheadcount = models.IntegerField()
    mayheadcount = models.IntegerField()
    junheadcount = models.IntegerField()
    julheadcount = models.IntegerField()
    augheadcount = models.IntegerField()
    sepheadcount = models.IntegerField()
    octheadcount = models.IntegerField()
    novheadcount = models.IntegerField()
    decheadcount = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'idc_vp_headcount_v'

class  IDCDomainHeadcountV(models.Model):
    id = models.BigIntegerField(primary_key=True)
    domain =   models.CharField(max_length=100, blank=True, null=True)        
    janheadcount = models.IntegerField()
    febheadcount = models.IntegerField()
    marheadcount = models.IntegerField()
    aprheadcount = models.IntegerField()
    mayheadcount = models.IntegerField()
    junheadcount = models.IntegerField()
    julheadcount = models.IntegerField()
    augheadcount = models.IntegerField()
    sepheadcount = models.IntegerField()
    octheadcount = models.IntegerField()
    novheadcount = models.IntegerField()
    decheadcount = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'idc_domain_headcount_v'


class  IDCDomainHoursV(models.Model):
    id = models.BigIntegerField(primary_key=True)
    domain =   models.CharField(max_length=100, blank=True, null=True)        
    janhrs = models.IntegerField()
    febhrs = models.IntegerField()
    marhrs = models.IntegerField()
    aprhrs = models.IntegerField()
    mayhrs = models.IntegerField()
    junhrs = models.IntegerField()
    julhrs = models.IntegerField()
    aughrs = models.IntegerField()
    sephrs = models.IntegerField()
    octhrs = models.IntegerField()
    novhrs = models.IntegerField()
    dechrs = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'idc_domain_hours_v'


class  IDCVPHoursV(models.Model):
    # id = models.BigIntegerField(primary_key=True)
    vicepresident =   models.CharField(max_length=100, blank=True, null=True)        
    jan = models.IntegerField()
    feb = models.IntegerField()
    mar = models.IntegerField()
    apr = models.IntegerField()
    may = models.IntegerField()
    jun = models.IntegerField()
    jul = models.IntegerField()
    aug = models.IntegerField()
    sep = models.IntegerField()
    oct = models.IntegerField()
    nov = models.IntegerField()
    dec = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'idc_vp_hours_v'


class  ATSVPVendorEmpV(models.Model):
    #id = models.BigIntegerField(primary_key=True)
    vicepresident =   models.CharField(max_length=100, blank=True, null=True)  
    monthyy =  models.CharField(max_length=30, blank=True, null=True)
    employee =  models.IntegerField()
    contractor =  models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ats_vp_vendoremp_v';

class  ATSDEPTVendorEmpV(models.Model):
    id = models.BigIntegerField(primary_key=True)
    department =   models.CharField(max_length=100, blank=True, null=True)  
    monthyy =  models.CharField(max_length=30, blank=True, null=True)
    employee =  models.IntegerField()
    contractor =  models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ats_dept_vendoremp_v';
