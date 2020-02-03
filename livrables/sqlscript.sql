CREATE SCHEMA IF NOT EXISTS `openfood` ;
USE `openfood` ;
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS `openfood`.`products` ;
DROP TABLE IF EXISTS `openfood`.`substituts` ;
DROP TABLE IF EXISTS `openfood`.`category` ;
SET foreign_key_checks = 1;
CREATE TABLE IF NOT EXISTS `openfood`.`category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `openfood`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(150) NULL,
  `description` VARCHAR(500) NULL,
  `store` VARCHAR(150) NULL,
  `nutri_score` VARCHAR(45) NULL,
  `url_product` VARCHAR(300) NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_products_category1_idx` (`category_id` ASC),
  CONSTRAINT `fk_products_category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `openfood`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB  CHARACTER SET utf8 COLLATE utf8_general_ci; 

CREATE TABLE IF NOT EXISTS `openfood`.`substituts` (
  `product_id` VARCHAR(45) NOT NULL,
  `substitut_id` INT NOT NULL,
  INDEX `fk_favoris_products1_idx` (`substitut_id` ASC),
  CONSTRAINT `fk_favoris_products1`
    FOREIGN KEY (`substitut_id`)
    REFERENCES `openfood`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
