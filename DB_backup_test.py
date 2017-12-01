#!/usr/bin/env python
# -*- encoding: utf-8 -*-

 
import pyodbc


connection = pyodbc.connect(driver='{SQL Server}', 
                                server='mislwmvdfs41', database='OFC_ECB', 
                                trusted_connection='yes', autocommit=True)
backup = "BACKUP DATABASE [OFC_ECB] TO DISK = N'H:\ecb.bak'"
cursor = connection.cursor().execute(backup)
connection.close()
