-- MySQL Script generated by MySQL Workbench
-- dim. 26 mai 2019 17:15:56 CEST
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema openfood
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema openfood
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `openfood` ;
USE `openfood` ;

-- -----------------------------------------------------
-- Table `openfood`.`category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfood`.`category` ;

CREATE TABLE IF NOT EXISTS `openfood`.`category` (
  `category_id` INT NOT NULL,
  `category_name` VARCHAR(45) NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openfood`.`products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfood`.`products` ;

CREATE TABLE IF NOT EXISTS `openfood`.`products` (
  `products_id` INT NOT NULL,
  `product_name` VARCHAR(45) NULL,
  `description` VARCHAR(150) NULL,
  `store` VARCHAR(45) NULL,
  `nutri_score` VARCHAR(45) NULL,
  `url_product` VARCHAR(45) NULL,
  `category_category_id` INT NOT NULL,
  PRIMARY KEY (`products_id`),
  INDEX `fk_products_category1_idx` (`category_category_id` ASC),
  CONSTRAINT `fk_products_category1`
    FOREIGN KEY (`category_category_id`)
    REFERENCES `openfood`.`category` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openfood`.`favoris`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfood`.`favoris` ;

CREATE TABLE IF NOT EXISTS `openfood`.`favoris` (
  `id_favory` INT NOT NULL,
  `product_id` VARCHAR(45) NULL,
  `products_products_id` INT NOT NULL,
  PRIMARY KEY (`id_favory`),
  INDEX `fk_favoris_products1_idx` (`products_products_id` ASC),
  CONSTRAINT `fk_favoris_products1`
    FOREIGN KEY (`products_products_id`)
    REFERENCES `openfood`.`products` (`products_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE = '';
DROP USER IF EXISTS yayass;
SET SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE USER 'yayass' IDENTIFIED BY 'test1234';

GRANT ALL ON `openfood`.* TO 'yayass';
GRANT SELECT ON TABLE `openfood`.* TO 'yayass';
GRANT SELECT, INSERT, TRIGGER ON TABLE `openfood`.* TO 'yayass';
GRANT SELECT, INSERT, TRIGGER, UPDATE, DELETE ON TABLE `openfood`.* TO 'yayass';
GRANT EXECUTE ON ROUTINE `openfood`.* TO 'yayass';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
