/*
 Navicat Premium Data Transfer

 Source Server         : 106.15.52.62_3306
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : 106.15.52.62:3306
 Source Schema         : qiaoliang

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 20/09/2022 10:52:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for activityInfo
-- ----------------------------
DROP TABLE IF EXISTS `activityInfo`;
CREATE TABLE `activityInfo`  (
  `activityID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `activityName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '心理活动名称',
  `activityOrganizer` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '举办单位',
  `activityIntroduce` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '活动介绍',
  `activityOrganizerID` int(11) UNSIGNED NOT NULL COMMENT '举办单位ID',
  `activityStartTime` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '开始时间',
  `activityPlace` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '活动举行地点',
  `activityEndTime` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '结束时间',
  `activityCreateTime` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `activityLastEditerID` int(11) UNSIGNED DEFAULT NULL COMMENT '最后编辑人ID\r\n\r\n',
  `activityLastEditTime` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '最后编辑时间',
  `activityNums` int(11) UNSIGNED DEFAULT NULL COMMENT '\r\n已报名人数',
  `activityMaxNums` int(11) UNSIGNED DEFAULT NULL COMMENT '最大人数',
  `picNum` int(5) UNSIGNED ZEROFILL DEFAULT NULL COMMENT '图片数',
  `activityLastEditer` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '最后编辑人',
  PRIMARY KEY (`activityID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 44 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for activityforUser
-- ----------------------------
DROP TABLE IF EXISTS `activityforUser`;
CREATE TABLE `activityforUser`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '用于保存每个活动的参与人数‘\r\n',
  `activityID` int(11) UNSIGNED DEFAULT NULL,
  `userID` int(11) UNSIGNED DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '状态',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for clubApply
-- ----------------------------
DROP TABLE IF EXISTS `clubApply`;
CREATE TABLE `clubApply`  (
  `clubID` int(11) UNSIGNED NOT NULL COMMENT '用于存储老师咨询信息',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `reasons` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '咨询理由',
  `applyID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `userAccount` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applyTime` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '时间',
  `status` int(1) UNSIGNED ZEROFILL DEFAULT 0 COMMENT '审核状态\r\n0-待审核\r\n1-通过\r\n2-拒绝',
  `reviewerName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '审核人',
  `reviewerID` int(11) UNSIGNED DEFAULT NULL COMMENT '审核人ID',
  `reviewTime` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '审核时间',
  PRIMARY KEY (`applyID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for clubHonor
-- ----------------------------
DROP TABLE IF EXISTS `clubHonor`;
CREATE TABLE `clubHonor`  (
  `clubID` int(11) UNSIGNED NOT NULL,
  `honorID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `honorName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '荣誉名称',
  `honorGrade` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '荣耀等级',
  `honorIssuer` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '颁发单位',
  `honorTime` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '获得时间',
  PRIMARY KEY (`honorID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for clubInfo
-- ----------------------------
DROP TABLE IF EXISTS `clubInfo`;
CREATE TABLE `clubInfo`  (
  `clubID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `clubName` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `clubNums` int(11) UNSIGNED ZEROFILL DEFAULT NULL COMMENT '咨询人数',
  `clubPic` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '头像',
  `clubChairman` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '姓名',
  `clubCharmanID` int(11) UNSIGNED DEFAULT NULL COMMENT '老师ID\r\n',
  `clubActivitiesNum` int(11) UNSIGNED ZEROFILL DEFAULT NULL COMMENT '好评数',
  `clubIntroduction` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '简介',
  `clubCategory` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '咨询类型',
  `clubUnit` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '个人信息',
  `clubHonorNums` int(11) UNSIGNED ZEROFILL DEFAULT NULL COMMENT '荣誉数目',
  PRIMARY KEY (`clubID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `RoleID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `RoleName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`RoleID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for userRole
-- ----------------------------
DROP TABLE IF EXISTS `userRole`;
CREATE TABLE `userRole`  (
  `userRoleID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `userID` int(11) UNSIGNED DEFAULT NULL,
  `roleID` int(11) UNSIGNED ZEROFILL DEFAULT NULL,
  `roleForClubID` int(11) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`userRoleID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
