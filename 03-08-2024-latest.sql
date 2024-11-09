/*
SQLyog Community v13.2.1 (64 bit)
MySQL - 10.4.32-MariaDB : Database - django_elevate
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`django_elevate` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;

USE `django_elevate`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=105 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can add permission',2,'add_permission'),
(5,'Can change permission',2,'change_permission'),
(6,'Can delete permission',2,'delete_permission'),
(7,'Can add group',3,'add_group'),
(8,'Can change group',3,'change_group'),
(9,'Can delete group',3,'delete_group'),
(10,'Can add user',4,'add_user'),
(11,'Can change user',4,'change_user'),
(12,'Can delete user',4,'delete_user'),
(13,'Can add content type',5,'add_contenttype'),
(14,'Can change content type',5,'change_contenttype'),
(15,'Can delete content type',5,'delete_contenttype'),
(16,'Can add session',6,'add_session'),
(17,'Can change session',6,'change_session'),
(18,'Can delete session',6,'delete_session'),
(19,'Can add animal',7,'add_animal'),
(20,'Can change animal',7,'change_animal'),
(21,'Can delete animal',7,'delete_animal'),
(22,'Can add complaint',8,'add_complaint'),
(23,'Can change complaint',8,'change_complaint'),
(24,'Can delete complaint',8,'delete_complaint'),
(25,'Can add contact',9,'add_contact'),
(26,'Can change contact',9,'change_contact'),
(27,'Can delete contact',9,'delete_contact'),
(28,'Can add crop',10,'add_crop'),
(29,'Can change crop',10,'change_crop'),
(30,'Can delete crop',10,'delete_crop'),
(31,'Can add event',11,'add_event'),
(32,'Can change event',11,'change_event'),
(33,'Can delete event',11,'delete_event'),
(34,'Can add farmer',12,'add_farmer'),
(35,'Can change farmer',12,'change_farmer'),
(36,'Can delete farmer',12,'delete_farmer'),
(37,'Can add harvesting',13,'add_harvesting'),
(38,'Can change harvesting',13,'change_harvesting'),
(39,'Can delete harvesting',13,'delete_harvesting'),
(40,'Can add leave',14,'add_leave'),
(41,'Can change leave',14,'change_leave'),
(42,'Can delete leave',14,'delete_leave'),
(43,'Can add login',15,'add_login'),
(44,'Can change login',15,'change_login'),
(45,'Can delete login',15,'delete_login'),
(46,'Can add plant',16,'add_plant'),
(47,'Can change plant',16,'change_plant'),
(48,'Can delete plant',16,'delete_plant'),
(49,'Can add task',17,'add_task'),
(50,'Can change task',17,'change_task'),
(51,'Can delete task',17,'delete_task'),
(52,'Can add transaction',18,'add_transaction'),
(53,'Can change transaction',18,'change_transaction'),
(54,'Can delete transaction',18,'delete_transaction'),
(55,'Can add worker',19,'add_worker'),
(56,'Can change worker',19,'change_worker'),
(57,'Can delete worker',19,'delete_worker'),
(58,'Can add inventory',20,'add_inventory'),
(59,'Can change inventory',20,'change_inventory'),
(60,'Can delete inventory',20,'delete_inventory'),
(61,'Can view log entry',1,'view_logentry'),
(62,'Can view permission',2,'view_permission'),
(63,'Can view group',3,'view_group'),
(64,'Can view user',4,'view_user'),
(65,'Can view content type',5,'view_contenttype'),
(66,'Can view session',6,'view_session'),
(67,'Can view animal',7,'view_animal'),
(68,'Can view contact',9,'view_contact'),
(69,'Can view crop',10,'view_crop'),
(70,'Can view farmer',12,'view_farmer'),
(71,'Can view login',15,'view_login'),
(72,'Can add workshop',21,'add_workshop'),
(73,'Can change workshop',21,'change_workshop'),
(74,'Can delete workshop',21,'delete_workshop'),
(75,'Can view workshop',21,'view_workshop'),
(76,'Can view worker',19,'view_worker'),
(77,'Can view transaction',18,'view_transaction'),
(78,'Can view task',17,'view_task'),
(79,'Can view plant',16,'view_plant'),
(80,'Can add payment',22,'add_payment'),
(81,'Can change payment',22,'change_payment'),
(82,'Can delete payment',22,'delete_payment'),
(83,'Can view payment',22,'view_payment'),
(84,'Can view leave',14,'view_leave'),
(85,'Can view inventory',20,'view_inventory'),
(86,'Can view harvesting',13,'view_harvesting'),
(87,'Can view event',11,'view_event'),
(88,'Can view complaint',8,'view_complaint'),
(89,'Can add workshops',23,'add_workshops'),
(90,'Can change workshops',23,'change_workshops'),
(91,'Can delete workshops',23,'delete_workshops'),
(92,'Can view workshops',23,'view_workshops'),
(93,'Can add payments',24,'add_payments'),
(94,'Can change payments',24,'change_payments'),
(95,'Can delete payments',24,'delete_payments'),
(96,'Can view payments',24,'view_payments'),
(97,'Can add worker_join',25,'add_worker_join'),
(98,'Can change worker_join',25,'change_worker_join'),
(99,'Can delete worker_join',25,'delete_worker_join'),
(100,'Can view worker_join',25,'view_worker_join'),
(101,'Can add fertilizer',26,'add_fertilizer'),
(102,'Can change fertilizer',26,'change_fertilizer'),
(103,'Can delete fertilizer',26,'delete_fertilizer'),
(104,'Can view fertilizer',26,'view_fertilizer');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'farmelevate_app','animal'),
(8,'farmelevate_app','complaint'),
(9,'farmelevate_app','contact'),
(10,'farmelevate_app','crop'),
(11,'farmelevate_app','event'),
(12,'farmelevate_app','farmer'),
(13,'farmelevate_app','harvesting'),
(14,'farmelevate_app','leave'),
(15,'farmelevate_app','login'),
(16,'farmelevate_app','plant'),
(17,'farmelevate_app','task'),
(18,'farmelevate_app','transaction'),
(19,'farmelevate_app','worker'),
(20,'farmelevate_app','inventory'),
(21,'farmelevate_app','workshop'),
(22,'farmelevate_app','payment'),
(23,'farmelevate_app','workshops'),
(24,'farmelevate_app','payments'),
(25,'farmelevate_app','worker_join'),
(26,'farmelevate_app','fertilizer');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-05-30 06:27:10.309712'),
(2,'auth','0001_initial','2024-05-30 06:27:10.528938'),
(3,'admin','0001_initial','2024-05-30 06:27:10.595904'),
(4,'admin','0002_logentry_remove_auto_add','2024-05-30 06:27:10.606219'),
(5,'contenttypes','0002_remove_content_type_name','2024-05-30 06:27:10.652303'),
(6,'auth','0002_alter_permission_name_max_length','2024-05-30 06:27:10.653185'),
(7,'auth','0003_alter_user_email_max_length','2024-05-30 06:27:10.679565'),
(8,'auth','0004_alter_user_username_opts','2024-05-30 06:27:10.691976'),
(9,'auth','0005_alter_user_last_login_null','2024-05-30 06:27:10.711402'),
(10,'auth','0006_require_contenttypes_0002','2024-05-30 06:27:10.712681'),
(11,'auth','0007_alter_validators_add_error_messages','2024-05-30 06:27:10.723885'),
(12,'auth','0008_alter_user_username_max_length','2024-05-30 06:27:10.746304'),
(13,'auth','0009_alter_user_last_name_max_length','2024-05-30 06:27:10.767794'),
(14,'farmelevate_app','0001_initial','2024-05-30 06:27:11.469916'),
(15,'sessions','0001_initial','2024-05-30 06:27:11.502459'),
(16,'farmelevate_app','0002_inventory','2024-05-30 08:14:25.946295'),
(17,'farmelevate_app','0003_contact','2024-05-30 09:00:39.931056'),
(18,'admin','0003_logentry_add_action_flag_choices','2024-06-26 14:57:55.990798'),
(19,'auth','0010_alter_group_name_max_length','2024-06-26 14:57:56.074413'),
(20,'auth','0011_update_proxy_permissions','2024-06-26 14:57:56.117298'),
(21,'auth','0012_alter_user_first_name_max_length','2024-06-26 14:57:56.153915');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('g64girj9fbsnxu3lduu6vwsoekr3fi10','NWY0NzBjYzMxODRiMTdmM2IzZWZiZTE4ZmVkZTQ5ZjMzYjc5YjgzNTp7ImxvZ2luX2lkIjoxLCJmYXJtZXJfaWQiOjEsIndfaWQiOjF9','2024-06-13 11:43:43.194489'),
('x2cnief9bwmax06tcsvjm2ejbiq5khnu','eyJsb2dpbl9pZCI6MywiZmFybWVyX2lkIjoyLCJ3X2lkIjozfQ:1sFsq0:DOYUYPsf7bXpVbQ-Ck5DRdd6dwlRkl-xfkzS6tBJQjg','2024-06-22 09:58:16.749984'),
('uzozcccubyraa10afk1gddnolazhxrwb','.eJyrVsrJT8_Mi89MUbIy1FFKSyzKTS0C84x0lMrBDBMdpRywdC0AUvMOBw:1sJW1W:pETPHSvnb6UUQFfE_HX8WElAzRrfdnS1Q_afzWbc03k','2024-07-02 10:25:10.472415'),
('fmq4zbcwdgraccj6qv8tql0qm3u931jo','eyJsb2dpbl9pZCI6MTUsImZhcm1lcl9pZCI6Miwid19pZCI6NH0:1sILFI:et1241R7Oy87UAgQIxsGRsSX74AsQiRz0TvvTrH1-OQ','2024-06-29 04:42:32.052072'),
('hg8k2udjwixbmiunjqxydqit6osf6t9h','eyJsb2dpbl9pZCI6MSwid19pZCI6NCwibGlkIjoxfQ:1sOc3q:4uOXQm4BCDqv36PBG53snJiBOSWf_82UWy6etn0eUkw','2024-07-16 11:52:38.690611'),
('ibhnuelkafq5fprl95mf0272miv19aiu','eyJsb2dpbl9pZCI6MTUsImxpZCI6MSwid19pZCI6NH0:1sNVqk:BnVzOSHeVHkV-bljpDS43PGAGqkRea54auS0rg_XD0U','2024-07-13 11:02:34.941364'),
('e77zlukuzm611mabmq8735kbilj1nadc','eyJsb2dpbl9pZCI6MSwid19pZCI6NCwibGlkIjoxfQ:1sMmq7:T1cdGQUcBpHAtVO9s7SoTEIdKH7UMHhDVkwcYedXPgE','2024-07-11 10:58:55.048463'),
('1xjeblt8n9z8pufb0vimykzjleafrg7d','eyJsb2dpbl9pZCI6MSwibGlkIjoxLCJ3X2lkIjozfQ:1sNSDC:OTX9le9bsIeV7vmn1NqmrH5UI-D4ifjoEyz28g_bktM','2024-07-13 07:09:30.015432'),
('g5a3ti1cfci9h5s8x3lzxd390l8456om','eyJsb2dpbl9pZCI6MTUsIndfaWQiOjR9:1sNSjm:g4HBJqFpUCZCnDvt-24s5qa3xAjUIhVycKY8i-6JwRo','2024-07-13 07:43:10.253228'),
('t122yaketfiorqd7by5o9ig9lyck5e84','eyJsb2dpbl9pZCI6MSwibGlkIjoxLCJ3X2lkIjo0fQ:1sZjbk:BpIC2tmIRwawCfFEMq2mqnZtZ6EfA64BAtUXaJV84IE','2024-08-16 04:09:36.816874'),
('fxonm6kp71gy6fxi5uasnmid1lxgqfbu','eyJsb2dpbl9pZCI6MSwibGlkIjoxLCJ3X2lkIjo0fQ:1sa5NO:c4gq1rOkuMkcQf7y8sIjSQZciWNf7-wte-TQlT1kHus','2024-08-17 03:24:14.362071');

/*Table structure for table `farmelevate_app_animal` */

DROP TABLE IF EXISTS `farmelevate_app_animal`;

CREATE TABLE `farmelevate_app_animal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `animal` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `breed` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `weight` decimal(5,2) NOT NULL,
  `breeding_status` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `documents` varchar(100) DEFAULT NULL,
  `internal_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_animal_farmer_id_a0efea74` (`internal_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_animal` */

insert  into `farmelevate_app_animal`(`id`,`animal`,`type`,`breed`,`gender`,`dob`,`status`,`weight`,`breeding_status`,`image`,`documents`,`internal_id`) values 
(17,'Bos taurus - Daisy','Cow','Jersey','Female','2024-06-07','Alive',56.00,'Not Breeding','cow3.jpeg','Cattle Document_vwhcrx6.pdf','CAT-003'),
(16,'Bos taurus - Maxx	','Bull','Angus','Male','2023-10-24','Alive',105.00,'Exposed','bull4 (1).jpeg','Cattle Document_3smmtyt_ukPP9P0.pdf','CAT-002'),
(15,'Bos taurus - Bella','Cattle','Holstein','Female','2023-06-12','Alive',89.00,'Not Breeding','cow1.jpeg','Cattle Document.pdf','CAT-001'),
(18,'Bos taurus - Duke','Bull	','Hereford','Male','2022-02-24','Alive',96.00,'Exposed','bull2.jpeg','Cattle Document_fDXxd7h.pdf','CAT-004'),
(19,'Bos taurus - Molly','Cow	','Simmental','Female','2021-02-25','Alive',89.00,'Lactacting','cow4.jpeg','Cattle Document_Z0kzaKH.pdf','CAT-005'),
(20,'Bubalus bubalis - Max','Bull','Surti','Male','2024-06-22','Alive',90.00,'Not Breeding','bull4.jpeg','Cattle Document_rmfCDik.pdf','CAT-006'),
(21,'Bubalus bubalis - Bella','Cow','Murrah','Female','2023-06-15','Alive',156.00,'Pregnant','cow6.jpeg','Cattle Document_xqGoeaf.pdf','BUF-001'),
(22,'szws','swsw','jersy','Male','1997-12-31','Sold',20.00,'Exposed','floor1image.jpeg','QP.-LOWER-DIVISION-CLERK-IN-KERALA-WATER-AUTHORITY-QC-106-2022-DOT-02.11.2022-1.pdf','ws'),
(23,'test','test','testn,j.','Female','2024-07-22','Alive',55.00,'Exposed','Mega-sale-600-×-360-px-30 (1).png','classic-vietnam-939758 (1).pdf','test'),
(24,'Bos taurus - Bella','Cow','Holstein','Female','2023-09-11','Alive',55.00,'Not Breeding','cow1 (5).jpeg','Cattle Document_zg83Ryq.pdf','cow1235');

/*Table structure for table `farmelevate_app_complaint` */

DROP TABLE IF EXISTS `farmelevate_app_complaint`;

CREATE TABLE `farmelevate_app_complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `Resolution_expt` varchar(100) NOT NULL,
  `complaint_text` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  `worker_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_complaint_farmer_id_4b83f088` (`farmer_id`),
  KEY `farmelevate_app_complaint_worker_id_763a8107` (`worker_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_complaint` */

insert  into `farmelevate_app_complaint`(`id`,`department`,`position`,`Resolution_expt`,`complaint_text`,`reply`,`date`,`farmer_id`,`worker_id`) values 
(2,'Planting','Worker','Irigation Pump Complaint','Irigation Pump Complaint','test','2024-06-22',1,3),
(5,'Planting','Worker','Tractor Repair','Tractor Repair','will rectify','2024-06-22',0,4),
(4,'Planting','Worker','Resource Unavialable','Resource Unavialable','will rectify','2024-06-14',0,4),
(8,'Planting','Worker','Tractor Repair','Tractor Repair','will do it soon','2024-06-24',0,4),
(9,'Planting','Worker','Tractor Repair','Tractor Repair','will rectify','2024-06-24',0,3),
(10,'Planting','Worker','Irigation Pump Complaint','Irigation Pump Complaint','will rectify','2024-06-24',0,4),
(11,'Planting','Worker','Rectify ASAP','Water Supply Down','pending','2024-06-24',0,4),
(12,'Planting','Worker','test','test','pending','2024-07-22',0,4),
(13,'Planting','Worker','dc','df','pending','2024-08-02',0,4);

/*Table structure for table `farmelevate_app_contact` */

DROP TABLE IF EXISTS `farmelevate_app_contact`;

CREATE TABLE `farmelevate_app_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Company` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_contact` */

insert  into `farmelevate_app_contact`(`id`,`Company`,`city`,`type`,`name`,`email`,`phone`) values 
(8,'Soft Tech','Kochi','Customer','Nesrin','nesrin@gmail.com','8956475136'),
(7,'Farm Fresh','Ernakulam','Customer','Dinesh','dinesh@gmail.com','8956461681'),
(5,'aish','kochi','Customer','aishh','aish@gmail.com','9856622556'),
(9,'DectoCart','Kozhikode','contractor','Raj Rajeev','rajdecto@gmail.com','7896412561'),
(10,'Farmzee','Ernakulam','Employee','Devika','devi@gmail.com','8954751256'),
(13,'test','test','Customer','test','test@gmail.com','9652355445'),
(14,'ARF FARM','Ernakulam','Customer',' Anilkumar','anilkumar33@gmail.com','9656842145');

/*Table structure for table `farmelevate_app_crop` */

DROP TABLE IF EXISTS `farmelevate_app_crop`;

CREATE TABLE `farmelevate_app_crop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  `variety` varchar(100) NOT NULL,
  `internal_id` varchar(50) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_crop_farmer_id_7544ca9c` (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_crop` */

insert  into `farmelevate_app_crop`(`id`,`type`,`variety`,`internal_id`,`farmer_id`) values 
(11,'Corn','Golden Jubilee','CRN-GJ-001',1),
(12,'Wheat','Hard Red Winter',' WHT-HRW-002',1),
(13,'Soybean','Envy','SBN-EV-003',1),
(14,'Tomato','Roma','TMT-RM-004',1),
(15,'Potato','Russet Burbank','PTO-RB-005',1),
(16,'Lettuce',' Butterhead','LET-BH-007',1),
(17,'Rice','Jasmine',' RCE-JS-006',1),
(18,'Carrot','Nantes','CRT-NT-008',1),
(19,'Apple','Fuji','APL-FJ-009',1),
(20,'Grape','Concord','GRP-CD-010',1),
(21,'testupdate','test','tsgx',1),
(22,'test','wheat','wh22335',1);

/*Table structure for table `farmelevate_app_event` */

DROP TABLE IF EXISTS `farmelevate_app_event`;

CREATE TABLE `farmelevate_app_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Event_title` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Start_date` varchar(100) NOT NULL,
  `End_date` varchar(100) NOT NULL,
  `Priority` varchar(100) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_event_farmer_id_458d260e` (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_event` */

insert  into `farmelevate_app_event`(`id`,`Event_title`,`Description`,`Start_date`,`End_date`,`Priority`,`farmer_id`) values 
(5,'Crop Rotation ','fds','2024-06-27','2024-06-05','low',1),
(4,'Irrigation','irigate ','2024-06-06','2024-06-20','high',2);

/*Table structure for table `farmelevate_app_farmer` */

DROP TABLE IF EXISTS `farmelevate_app_farmer`;

CREATE TABLE `farmelevate_app_farmer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `farm_name` varchar(100) NOT NULL,
  `farm_address` varchar(100) NOT NULL,
  `farm_size` varchar(100) NOT NULL,
  `farm_type` varchar(100) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_farmer_login_id_1511272f` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_farmer` */

insert  into `farmelevate_app_farmer`(`id`,`first_name`,`last_name`,`dob`,`gender`,`phone`,`email`,`address`,`country`,`farm_name`,`farm_address`,`farm_size`,`farm_type`,`login_id`) values 
(1,'Aiswarya','Anilkumar','2000-11-21','Female','8954123568','aiswaryaanilkumar@gmail.com','123A Hill Plaza ','India','Farmzee','1344A Ploat Hillzade , Kochi Keerala','366 acres','Mixed',1);

/*Table structure for table `farmelevate_app_fertilizer` */

DROP TABLE IF EXISTS `farmelevate_app_fertilizer`;

CREATE TABLE `farmelevate_app_fertilizer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `soil_type` varchar(100) DEFAULT NULL,
  `crop_type` varchar(100) DEFAULT NULL,
  `temperature` varchar(100) DEFAULT NULL,
  `humidity` varchar(100) DEFAULT NULL,
  `moisture` varchar(100) DEFAULT NULL,
  `nitrogen` varchar(100) DEFAULT NULL,
  `potassium` varchar(100) DEFAULT NULL,
  `phosphorus` varchar(100) DEFAULT NULL,
  `out` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_fertilizer` */

insert  into `farmelevate_app_fertilizer`(`id`,`soil_type`,`crop_type`,`temperature`,`humidity`,`moisture`,`nitrogen`,`potassium`,`phosphorus`,`out`) values 
(1,'3','2','9','5','13','5','5','9','5'),
(2,'4','4','59','1','8999999999999999999','2','26','6','7'),
(3,'4','4','59','1','6','2','26','6','7'),
(4,'7','3','5','4','4','5','4','4','1'),
(5,'4','1','4','4','5','1','8','4','1');

/*Table structure for table `farmelevate_app_harvesting` */

DROP TABLE IF EXISTS `farmelevate_app_harvesting`;

CREATE TABLE `farmelevate_app_harvesting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `variety` varchar(100) NOT NULL,
  `internal_id` varchar(50) NOT NULL,
  `location_type` varchar(100) NOT NULL,
  `size` varchar(100) NOT NULL,
  `harvesting_date` varchar(200) NOT NULL,
  `crop_id` int(11) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `worker_id` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_harvesting_crop_id_5e8a548e` (`crop_id`),
  KEY `farmelevate_app_harvesting_farmer_id_13aad4d5` (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_harvesting` */

insert  into `farmelevate_app_harvesting`(`id`,`name`,`variety`,`internal_id`,`location_type`,`size`,`harvesting_date`,`crop_id`,`farmer_id`,`status`,`worker_id`) values 
(3,'Tomato Red','Tomato','TM-LJ-001','GrowRoom','12','2024-07-11',2,2,'completed','4'),
(2,'Rice','Basmathi','BA-BS-002','Field','12','2024-06-28',2,2,'completed','4'),
(8,'Tomato Red','Tomato','TM-LJ-001','GrowRoom','56','2024-06-13',2,1,'completed','4'),
(5,'Rice','Basmathi','BA-BS-002','Field','900','2024-06-18',2,1,'completed','3'),
(9,'Sweet Corn','Golden Jubilee','CRN-GJ-001','Field','45','2024-06-30',11,1,'completed','4'),
(10,'Tomato Small Red','Roma','TMT-RM-004','GreenHouse','45','2024-07-04',14,1,'completed','4'),
(11,'Soy B234','Envy','SBN-EV-003','Field','45','2024-07-01',13,1,'completed','4'),
(12,'test','test','tsgx','Field','41','2024-08-01',21,1,'pending','4'),
(13,'Wheat - 12RW','Hard Red Winter',' WHT-HRW-002','Field','45','2024-08-21',12,1,'pending','4');

/*Table structure for table `farmelevate_app_inventory` */

DROP TABLE IF EXISTS `farmelevate_app_inventory`;

CREATE TABLE `farmelevate_app_inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `ls` varchar(100) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_inventory_farmer_id_02f348d1` (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_inventory` */

insert  into `farmelevate_app_inventory`(`id`,`name`,`type`,`brand`,`model`,`ls`,`farmer_id`) values 
(8,'Delivery Truck','DEL YT34','VOLVO','DEL YT34','2024-07-05',1),
(5,'van','VAN ER23','TOYOTA','VAN ER23','2024-06-20',1),
(6,'showel','SHA TY34','NIDAVA','TRA QCA4','none',1),
(7,'Tractor','TRA TQS5','TOYOTAA','TRA TQS5','2024-06-21',1),
(9,'Equipment Q23','EQU 15L4','TOYOTA','EQU 15L4','none',1),
(10,'Delivery Truck','DEL 458S','SCANIA','DEL 458S','2024-07-05',1),
(11,'TRACTOR','TRA QCA2','TOYOTA','QWS1234','none',1),
(12,'test','testad','test','test','2024-07-22',1);

/*Table structure for table `farmelevate_app_leave` */

DROP TABLE IF EXISTS `farmelevate_app_leave`;

CREATE TABLE `farmelevate_app_leave` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `Reason` varchar(100) NOT NULL,
  `leave_type` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `startdate` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  `worker_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_leave_farmer_id_ac9ece68` (`farmer_id`),
  KEY `farmelevate_app_leave_worker_id_5f91dc1a` (`worker_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_leave` */

insert  into `farmelevate_app_leave`(`id`,`department`,`position`,`Reason`,`leave_type`,`total`,`startdate`,`status`,`date`,`farmer_id`,`worker_id`) values 
(3,'Planting','worker','sick','sick','2','2024-06-16','Rejected','2024-06-21',1,4),
(2,'Planting','worker','personal','sick','10','2024-07-02','Rejected','2024-06-19',2,3),
(1,'irigation','worker','fever','sick','10','2024-06-19','Accepted','2024-06-19',2,4),
(4,'Planting','worker','Sick','sick','5','2024-06-24','Accepted','2024-07-06',1,4),
(5,'Planting','Worker','Fever','sick','5','2024-06-26','Accepted','2024-06-26',1,4),
(6,'Planting','Worker','Sick','sick','2','2024-06-25','Rejected','2024-06-29',1,4),
(7,'Planting','Worker','Fever','sick','2','2024-06-28','Accepted','2024-06-29',1,3),
(8,'Planting','Worker','Sick','sick','5','2024-06-29','Rejected','2024-07-06',1,3),
(9,'Planting','Worker','Fever','sick','2','2024-06-28','Accepted','2024-06-27',1,4),
(10,'Planting','Worker','test','sick','5','2024-07-24','pending','2024-08-05',1,4),
(11,'Planting','Worker','qww','vaccation','2','2024-08-20','Accepted','2024-08-21',1,4);

/*Table structure for table `farmelevate_app_login` */

DROP TABLE IF EXISTS `farmelevate_app_login`;

CREATE TABLE `farmelevate_app_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `usertype` varchar(150) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_login` */

insert  into `farmelevate_app_login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','Admin@123','admin'),
(15,'sree','Sree@123','worker'),
(3,'aish','aish','farmer'),
(4,'nes','nes','pending'),
(5,'nesrin','nesrin','pending'),
(6,'reema','reema','pending'),
(7,'nesrin','','pending'),
(8,'nesrin','','pending'),
(9,'nesrin','123445','pending'),
(10,'nesrin','sxsxswdswd','pending'),
(11,'nes','2erfrgc','pending'),
(12,'nes','fvfffdfc','pending'),
(14,'haritha','Haritha@123','worker');

/*Table structure for table `farmelevate_app_payments` */

DROP TABLE IF EXISTS `farmelevate_app_payments`;

CREATE TABLE `farmelevate_app_payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `workshop_id` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `cname` varchar(100) DEFAULT NULL,
  `cnumber` varchar(100) DEFAULT NULL,
  `cvv` varchar(100) DEFAULT NULL,
  `expiry` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_payments` */

insert  into `farmelevate_app_payments`(`id`,`workshop_id`,`worker_id`,`cname`,`cnumber`,`cvv`,`expiry`,`amount`) values 
(9,11,4,'sree','7894 5621 4521 5588','5555','12/24','500'),
(10,16,4,'Sreeka','8451 2187 9563 2014','8956','12/24','500'),
(11,17,4,'dxfgvbh','9745 1207 9653 2156','6521','11/24','500'),
(12,18,4,'esrjm','9562 0798 5625 9886','8965','12/24','200'),
(13,19,4,'cfvgbn','9461 2653 5374 1245','6321','12/24','550'),
(14,20,4,'sreeka','7894 5642 2685 2356','7894','12/24','500'),
(15,16,3,'haritha','8956 2341 2566 5551','5623','12/24','500');

/*Table structure for table `farmelevate_app_plant` */

DROP TABLE IF EXISTS `farmelevate_app_plant`;

CREATE TABLE `farmelevate_app_plant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `variety` varchar(100) NOT NULL,
  `internal_id` varchar(50) NOT NULL,
  `location_type` varchar(100) NOT NULL,
  `planting_fomate` varchar(100) NOT NULL,
  `Plant_date` varchar(200) NOT NULL,
  `crop_id` int(11) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_plant_crop_id_1be74b46` (`crop_id`),
  KEY `farmelevate_app_plant_farmer_id_c305c112` (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_plant` */

insert  into `farmelevate_app_plant`(`id`,`name`,`variety`,`internal_id`,`location_type`,`planting_fomate`,`Plant_date`,`crop_id`,`farmer_id`,`status`,`worker_id`) values 
(10,'Spinach Red','Spinach ','SPI-SP-006','GrowRoom','Row Crop','2024-06-07',2,1,'completed',4),
(3,'Sweet Corn','Golden Jubilee','CRN-GJ-001','GrowRoom','Row Crop','2024-06-20',2,1,'completed',4),
(2,'Tomato Red','Roma','TMT-RM-004','Field','Planted In Bed','2024-06-18',2,1,'completed',3),
(11,'Sweet Corn','Golden Jubilee','CRN-GJ-001','GreenHouse','Planted In Bed','2024-06-28',11,1,'completed',3),
(12,'Tomato Red','Roma','TMT-RM-004','GrowRoom','Planted In Bed','2024-06-27',14,1,'completed',4),
(13,'Potato High Quality','Russet Burbank','PTO-RB-005','Field','Planted In Bed','2024-07-05',15,1,'completed',4),
(14,'Sweet Corn','Golden Jubilee','CRN-GJ-001','GreenHouse','corner Crop','2024-07-06',11,1,'completed',4),
(15,'Bay Wheat','Hard Red Winter',' WHT-HRW-002','Field','Planted In Bed','2024-07-04',12,1,'completed',4),
(16,'test','test','tsgx','GrowRoom','corner Crop','2024-07-27',21,1,'completed',4),
(17,'Lettuce-Green',' Butterhead','LET-BH-007','Field','Planted In Bed','2024-08-31',16,1,'pending',4);

/*Table structure for table `farmelevate_app_task` */

DROP TABLE IF EXISTS `farmelevate_app_task`;

CREATE TABLE `farmelevate_app_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(200) NOT NULL,
  `due_date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `Priority` varchar(100) NOT NULL,
  `assigned_worker_id` int(11) DEFAULT NULL,
  `farmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_task_assigned_worker_id_3b7aa648` (`assigned_worker_id`),
  KEY `farmelevate_app_task_farmer_id_f27336c7` (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_task` */

insert  into `farmelevate_app_task`(`id`,`task_name`,`due_date`,`status`,`description`,`Priority`,`assigned_worker_id`,`farmer_id`) values 
(31,'Herding Livestock','2024-08-17','completed','Move the livestock to different pastures or pens as needed','Low',3,1),
(30,'Maintaining Greenhouses','2024-06-30','completed','Check the greenhouse conditions, water the plants, and ensure temperature and humidity are optimal','High',4,1),
(27,'Milking Cows','2024-07-10','pending','Milk the cows and ensure the milking equipment is clean before and after use.','Medium',3,1),
(28,'Composting','2024-06-27','completed','Collect organic waste and add it to the compost pile. Turn the compost to aerate it.','Low',4,1),
(29,'Sorting and Grading Produce','2024-07-26','pending','Sort and grade the harvested produce according to quality and size.','Low',3,1),
(20,'Weed Control','2024-07-19','completed','Go through the fields and remove any weeds. Use the hoe for small weeds and herbicide for larger areas.','Low',4,1),
(26,'Spraying Pesticides','2024-06-29','pending','Spray the crops with pesticides to protect them from pests. Follow safety guideline\r\nField :FEI12345','High',3,1),
(24,'Checking Machinery','2024-07-30','completed','Inspect all farming equipment and machinery. Perform maintenance and repairs as needed.','Medium',4,1),
(25,'Cleaning Barns','2024-06-28','pending','Clean out the barns. Remove any old bedding and manure, and replace it with fresh straw.','Medium',3,1),
(23,'Repairing Fences','2024-08-02','completed','Inspect the fences and repair any broken sections to keep the livestock contained','Low',4,1),
(22,'Feeding Livestock','2024-06-25','completed','Make sure all the animals are fed. Check their water supply and fill it if necessary.','High',3,1),
(21,'Fertilizing Fields','2024-06-28','pending','Spread fertilizer evenly across the fields to ensure the crops get the necessary nutrients\r\nuse fertilizer :urea','Medium',4,1),
(18,'Plowing Fields','2024-06-29','completed','Take the tractor and plow the fields. The soil needs to be turned over and broken up for planting.','High',3,1),
(19,'Irrigation Management','2024-07-18','completed','Check the irrigation systems and ensure all areas are getting enough water. Adjust the schedule if needed for even watering','Medium',4,1),
(33,'test','2024-08-01','pending','tets','Medium',4,1),
(34,'fertilizing','2024-08-21','completed','xzcv','High',3,1);

/*Table structure for table `farmelevate_app_transaction` */

DROP TABLE IF EXISTS `farmelevate_app_transaction`;

CREATE TABLE `farmelevate_app_transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `payee` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `type` varchar(7) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `bill` varchar(100) DEFAULT NULL,
  `farmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farmelevate_app_transaction_farmer_id_ebe2d4ed` (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_transaction` */

insert  into `farmelevate_app_transaction`(`id`,`date`,`payee`,`category`,`type`,`amount`,`bill`,`farmer_id`) values 
(5,'2024-06-14','lice John','Agritourism Events','income',10000.00,'login.PNG',2),
(4,'2024-06-14','Dr. David Brown','Medical consultation fee paid to Dr. David Brown','Expense',289.00,'ecom2.PNG',2),
(2,'2024-06-08','Jane Doe','Tractor Repair Services','Expense',500.00,'error_zip (1).png',2),
(1,'2024-06-21','John Smith',' Livestock Sales Inc.','income',500.00,'manufactureregister.PNG',2),
(6,'2024-06-22','Mark Johnson','Seed Supplier Inc.','Expense',200.00,'payment_2hs5wJv.jpeg',2),
(7,'2024-06-22','Wilson Bark','Farm Events and Workshops','Income',5000.00,'payment_pJzyswP.jpeg',1),
(8,'2024-06-23','Peter Pondey','EquimenFarmhands Labor Co.t QWE349','Expense',900.00,'error_zip.png',1),
(9,'2024-06-23','Micheal Baurl','Organic Produce Co.','Income',9600.00,'error_zip (1).png',1),
(10,'2024-06-23','Carol Caris','Farm Stand Sales','Income',50000.00,'error_zip (1)_mPDJpbR.png',1),
(11,'2024-06-23','francis','Equiment QWE349','Income',2000.00,'error_zip (1)_Gf8dfiB.png',1),
(12,'2024-06-23','Latisha Lali','Equiment QWE349','Expense',1000.00,'error_zip (1)_5mzdgs6.png',1),
(13,'2024-06-23','Shone Menze','Agricultural Chemicals Supplier','Expense',2000.00,'error_zip (1)_xdXLwwt.png',1),
(14,'2024-06-24','Puthina Pursh','Farm Rentals','Income',5000.00,'ecom2 (3).PNG',1),
(15,'2024-07-22','testm,.','test','Income',1000.00,'classic-vietnam-939758 (1)_aOkOmJV.pdf',1),
(16,'2024-08-02','jerry','Equiment QWE349','Income',52000.00,'farmelevate-usecase.pdf',1);

/*Table structure for table `farmelevate_app_worker` */

DROP TABLE IF EXISTS `farmelevate_app_worker`;

CREATE TABLE `farmelevate_app_worker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` longtext NOT NULL,
  `country` varchar(100) NOT NULL,
  `login_id` int(11) NOT NULL,
  `emp_id` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `farmelevate_app_worker_login_id_09dc60b3` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_worker` */

insert  into `farmelevate_app_worker`(`id`,`first_name`,`last_name`,`dob`,`gender`,`phone`,`email`,`address`,`country`,`login_id`,`emp_id`,`position`,`department`) values 
(3,'Haritha','T H','2024-06-18','Female','8956412563','haritha@gmail.com','145C Viewdaze Kochi','india',14,'EMP012345','Manager','Irigation'),
(4,'Sreeka','k','1987-09-14','Female','9564213586','sree@gmail.com','124A Martian Plaza Kochi','india',15,'EMP056789','Worker','Planting'),
(5,'Reema','Rafeek','2001-02-19','Female','9785451356','reema@gmail.com','234A Nilzede Kochi','India',16,'EMP025654','Worker','Planting');

/*Table structure for table `farmelevate_app_worker_join` */

DROP TABLE IF EXISTS `farmelevate_app_worker_join`;

CREATE TABLE `farmelevate_app_worker_join` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `workshop_id` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `planguage` varchar(100) DEFAULT NULL,
  `education` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_worker_join` */

insert  into `farmelevate_app_worker_join`(`id`,`workshop_id`,`worker_id`,`planguage`,`education`,`amount`) values 
(2,13,4,'english','mcom','500'),
(4,16,4,'malayalam','Mcom','500'),
(5,17,4,'malayalam','Mcom','500'),
(6,18,4,'malayalam','Mcom','200'),
(7,19,4,'malayalam','Mcom','550'),
(8,11,4,'malayalam','Mcom','522'),
(9,20,4,'malayalam','Mcom','500'),
(10,16,3,'malayalam','BSc Biology','500');

/*Table structure for table `farmelevate_app_workshop` */

DROP TABLE IF EXISTS `farmelevate_app_workshop`;

CREATE TABLE `farmelevate_app_workshop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `date_time` datetime NOT NULL,
  `location` varchar(100) NOT NULL,
  `no_of_slots` varchar(100) NOT NULL,
  `reg_fees` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `farmelevate_app_workshop` */

insert  into `farmelevate_app_workshop`(`id`,`title`,`description`,`date_time`,`location`,`no_of_slots`,`reg_fees`,`status`) values 
(13,'aaa','asxcdx','2024-07-02 13:52:00','kochi','30','300','expired'),
(16,'Organic Farming Techniques',' Explore methods to grow crops organically, enhance soil health, and reduce chemical use.','2024-07-26 15:17:00','kochi','3','500','pending'),
(17,'test','test','2024-08-19 14:40:00','kochi','4','500','pending'),
(18,'test2','tst\'','2024-07-22 00:15:00','kochi','4','200','pending'),
(19,'test3','test','2024-07-22 14:16:00','kochi','4','550','pending'),
(20,'Fertilizing','Fertlizing','2024-08-16 14:39:00','kochi','4','500','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
