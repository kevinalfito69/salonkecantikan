import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Transaksi:
    def __init__(self):
        self.__id_transaksi= None
        self.__kode_transaksi= None
        self.__tanggal_transaksi= None
        self.__specialis= None
        self.__nama_pelanggan= None
        self.__keterangan= None
        self.__total= None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id_transaksi(self):
        return self.__id_transaksi
    
    @property
    def kode_transaksi(self):
        return self.__kode_transaksi

    @kode_transaksi.setter
    def kode_transaksi(self, value):
        self.__kode_transaksi = value
    
    @property
    def tanggal_transaksi(self):
        return self.__tanggal_transaksi

    @tanggal_transaksi.setter
    def tanggal_transaksi(self, value):
        self.__tanggal_transaksi = value
    
    @property
    def specialis(self):
        return self.__specialis

    @specialis.setter
    def specialis(self, value):
        self.__specialis = value

    @property
    def nama_pelanggan(self):
        return self.__nama_pelanggan

    @nama_pelanggan.setter
    def nama_pelanggan(self, value):
        self.__nama_pelanggan = value
    
    @property
    def keterangan(self):
        return self.__keterangan

    @keterangan.setter
    def keterangan(self, value):
        self.__keterangan = value
        
    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_transaksi,self.__tanggal_transaksi,self.__specialis)
        sql="INSERT INTO transaksi(kode_transaksi,tanggal_transaksi,specialis) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_transaksi,self.__tanggal_transaksi,self.__specialis, id)
        sql="UPDATE transaksi SET kode_transaksi=%s, tanggal_transaksi=%s, specialis=%s WHERE id_transaksi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateBykode_transaksi(self, kode_transaksi):
        self.conn = mydb()
        val = (self.__kode_transaksi,self.__tanggal_transaksi,self.__specialis, kode_transaksi)
        sql="UPDATE transaksi SET kode_transaksi=%s, tanggal_transaksi=%s, specialis=%s WHERE kode_transaksi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM transaksi WHERE id_transaksi='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteBykode_transaksi(self, kode_transaksi):
        self.conn = mydb()
        sql="DELETE FROM transaksi WHERE kode_transaksi='" + str(kode_transaksi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM transaksi WHERE id_transaksi='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_transaksi = self.result[1]                   
        self.__tanggal_transaksi = self.result[2]                   
        self.__specialis = self.result[3]                   
        self.conn.disconnect
        return self.result
        
    def getBykode_transaksi(self, kode_transaksi):
        a=str(kode_transaksi)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM transaksi WHERE kode_transaksi='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_transaksi = self.result[1]
            self.__tanggal_transaksi = self.result[2]
            self.__specialis = str(self.result[3])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_transaksi = ''                  
            self.__tanggal_transaksi = ''                  
            self.__specialis = ''                  
            self.affected = 0
        self.conn.disconnect
        return self.result
        
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM transaksi limit 100"
        self.result = self.conn.findAll(sql)
        return self.result