import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Produk:

    def __init__(self):
        self.__id_produk=None
        self.__kode_produk=None
        self.__nama_produk=None
        self.__kode_kategori=None
        self.__harga=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "kode_produk:" + self.__kode_produk + "\n" + "nama_produk:" + self.__nama_produk + "\n" + "kode_kategori" + self.__kode_kategori + "\n" + "Harga:" + self.__harga
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id_produk(self):
        return self.__id_produk

    @property
    def kode_produk(self):
        return self.__kode_produk

    @kode_produk.setter
    def kode_produk(self, value):
        self.__kode_produk = value

    @property
    def nama_produk(self):
        return self.__nama_produk

    @nama_produk.setter
    def nama_produk(self, value):
        self.__nama_produk = value

    @property
    def kode_kategori(self):
        return self.__kode_kategori

    @kode_kategori.setter
    def kode_kategori(self, value):
        self.__kode_kategori = value

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_produk, self.__nama_produk, self.__kode_kategori, self.__harga)
        sql="INSERT INTO produk(kode_produk, nama_produk, kode_kategori, harga) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_produk, self.__nama_produk, self.__kode_kategori, self.__harga, id)
        sql="UPDATE produk SET kode_produk = %s, nama_produk = %s, kode_kategori=%s, harga=%s WHERE id_produk=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode_produk(self, kode_produk__kode_produk):
        self.conn = mydb()
        val = (self.__nama_produk, self.__kode_kategori, self.__harga, kode_produk__kode_produk)
        sql="UPDATE produk SET nama_produk = %s, kode_kategori__kode_kategori=%s, harga=%s WHERE kode_produk__kode_produk=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM produk WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykode_produk(self, kode_produk__kode_produk):
        self.conn = mydb()
        sql="DELETE FROM produk WHERE kode_produk='" + str(kode_produk__kode_produk) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM produk WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_produk = self.result[1]
        self.__nama_produk = self.result[2]
        self.__kode_kategori = self.result[3]
        self.__harga = self.result[4]
        self.conn.disconnect
        return self.result

    def getBykode_produk(self, kode_produk):
        self.conn = mydb()
        sql="SELECT * FROM produk WHERE kode_produk=" + str(kode_produk) + ""
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_produk = self.result[1]
            self.__nama_produk = self.result[2]
            self.__kode_kategori = self.result[3]
            self.__harga = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_produk = ''
            self.__nama_produk = ''
            self.__kode_kategori = ''
            self.__harga = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM produk limit 100"
        self.result = self.conn.findAll(sql)
        return self.result