from distutils.log import info
import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Kategori:

    def __init__(self):
        self.__id=None
        self.__kode_kategori=None
        self.__nama_kategori=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "kode_kategori:" + self.__kode_kategori + "\n" + "nama_kategori:" + self.__nama_kategori + "\n"
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def kode_kategori(self):
        return self.__kode_kategori

    @kode_kategori.setter
    def kode_kategori(self, value):
        self.__kode_kategori = value

    @property
    def nama_kategori__nama_kategori(self):
        return self.__nama_kategori

    @nama_kategori__nama_kategori.setter
    def nama_kategori__nama_kategori(self, value):
        self.__nama_kategori = value


    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_kategori, self.__nama_kategori)
        sql="INSERT INTO kategori (kode_kategori, nama_kategori) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_kategori, self.__nama_kategori, id)
        sql="UPDATE kategori SET kode_kategori=%s, nama_kategori= %s, WHERE idkategori=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode_kategori(self, kode_kategori):
        self.conn = mydb()
        val = (self.__nama_kategori, kode_kategori)
        
        sql="UPDATE kategori SET nama_kategori=%s WHERE kode_kategori=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE idkategori='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykode_kategori(self, kode_kategori):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE kode_kategori='" + str(kode_kategori) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE idkategori='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_kategori = self.result[1]
        self.__nama_kategori = self.result[2]
        self.conn.disconnect
        return self.result

    def getBykode_kategori(self, kode_kategori):
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE kode_kategori='" + str(kode_kategori) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_kategori = self.result[1]
            self.__nama_kategori = self.result[2]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_kategori = ''
            self.__nama_kategori = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM kategori limit 100"
        self.result = self.conn.findAll(sql)
        return self.result