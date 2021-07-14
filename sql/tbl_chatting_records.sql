/*
Navicat MySQL Data Transfer

Source Server         : 2Executioner
Source Server Version : 50731
Source Host           : localhost:3306
Source Database       : agc

Target Server Type    : MYSQL
Target Server Version : 50731
File Encoding         : 65001

Date: 2021-07-11 08:34:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tbl_chatting_records
-- ----------------------------
DROP TABLE IF EXISTS `tbl_chatting_records`;
CREATE TABLE `tbl_chatting_records` (
  `id` char(32) NOT NULL,
  `user_id` char(32) DEFAULT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除(1:已删除，0:未删除)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
