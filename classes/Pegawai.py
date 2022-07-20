import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Pegawai:

    def __init__(self):
        self.__idPegawai=None
        self.__kode_pegawai=None
        self.__nama=None
        self.__posisi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "kode_pegawai:" + self.__kode_pegawai + "\n" + "nama" + self.__nama + "\n"+ "posisi" +  self.__posisi
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idPegawai(self):
        return self.__idPegawai

    @property
    def kode_pegawai(self):
        return self.__kode_pegawai

    @kode_pegawai.setter
    def kode_pegawai(self, value):
        self.__kode_pegawai = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def posisi(self):
        return self.__posisi

    @posisi.setter
    def posisi(self, value):
        self.__posisi= value


    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_pegawai, self.__nama, self.__posisi)
        sql="INSERT INTO pegawai (kode_pegawai,nama,posisi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_pegawai, self.__nama,self.__posisi, id)
        sql="UPDATE pegawai SET kode_pegawai=%s, nama=%s, posisi=%s, WHERE idpegawai=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode_pegawai(self, kode_pegawai):
        self.conn = mydb()
        val = (self.__nama,self.__posisi, kode_pegawai)
        sql="UPDATE pegawai SET nama=%s, posisi=%s WHERE kode_pegawai=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM pegawai WHERE idpegawai='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykode_pegawai(self, kode_pegawai):
        self.conn = mydb()
        sql="DELETE FROM pegawai WHERE kode_pegawai='" + str(kode_pegawai) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, idPegawai):
        self.conn = mydb()
        sql="SELECT * FROM pegawai WHERE idpegawai='" + str(idPegawai) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_pegawai = self.result[1]
        self.__nama = self.result[2]
        self.__posisi = self.result[3]

        self.conn.disconnect
        return self.result

    def getBykode_pegawai(self, kode_pegawai):
        self.conn = mydb()
        sql="SELECT * FROM pegawai WHERE kode_pegawai='" + str(kode_pegawai) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_pegawai = self.result[1]
            self.__nama = self.result[2]
            self.__posisi= self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_pegawai = ''
            self.__nama = ''
            self.__posisi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pegawai limit 100"
        self.result = self.conn.findAll(sql)
        return self.result