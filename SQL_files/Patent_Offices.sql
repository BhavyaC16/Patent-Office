CREATE TABLE Patent_Offices(
   Office_ID             INTEGER  NOT NULL PRIMARY KEY 
  ,Office_Location       VARCHAR(7) NOT NULL
  ,Office_Postal_Address VARCHAR(87) NOT NULL
  ,Office_Website        VARCHAR(25) NOT NULL
  ,Office_Contact        VARCHAR(21) NOT NULL
);
INSERT INTO Patent_Offices(Office_ID,Office_Location,Office_Postal_Address,Office_Website,Office_Contact) VALUES (1,'Delhi','Intellectual Property Office Building, Plot No. 32, Sector 14, Dwarka, New Delhi-110078','http://www.ipindia.nic.in','delhi-patent@nic.in');
INSERT INTO Patent_Offices(Office_ID,Office_Location,Office_Postal_Address,Office_Website,Office_Contact) VALUES (2,'Mumbai','Boudhik Sampada Bhawan, Antop Hill, S. M. Road, Mumbai - 400 037.','http://www.ipindia.nic.in','mumbai-patent@nic.in');
INSERT INTO Patent_Offices(Office_ID,Office_Location,Office_Postal_Address,Office_Website,Office_Contact) VALUES (3,'Chennai','Patent Office Intellectual Property Building G.S.T. Road, Guindy, Chennai-600032','http://www.ipindia.nic.in','chennai-patent@nic.in');
INSERT INTO Patent_Offices(Office_ID,Office_Location,Office_Postal_Address,Office_Website,Office_Contact) VALUES (4,'Kolkata','Intellectual Property Office Building, CP-2 Sector V, Salt Lake City,Kolkata-700091','http://www.ipindia.nic.in','kolkata-patent@nic.in');
