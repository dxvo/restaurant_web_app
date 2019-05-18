


CREATE TABLE log_in (
  User_ID int(8) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
  UserName varchar(20) NOT NULL,
  Password_Hash varchar(72) NOT NULL,
  PRIMARY KEY (User_ID)
); 



CREATE TABLE `Food_Info` (
  `food_id` INT NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `calorie` int(11) DEFAULT NULL,
  `has_image` tinyint(3) unsigned NOT NULL,
  `menu_price` int(11) NOT NULL,
  `material_cost` int(11) NOT NULL,
  PRIMARY KEY (`food_id`),
  UNIQUE KEY `idproducts_UNIQUE` (`food_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



CREATE TABLE `Transaction` (
`transanction_id` INT  NOT NULL,
  `food_id` INT NOT NULL,
  `food_name` varchar(50) NOT NULL,
  `quanlity` int(11) NOT NULL,
  PRIMARY KEY (`transanction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



CREATE TABLE `vrjw534e3pgu7qdo`.`Survey` (
  `transanction_id` INT  NOT NULL,
  `gender` VARCHAR(6) NOT NULL,
  `ethnicity` VARCHAR(15) NOT NULL,
  `age` INT NOT NULL,
  `zipcode` INT NOT NULL,
  PRIMARY KEY (`transanction_id`),
  UNIQUE INDEX `transanction_id_UNIQUE` (`transanction_id` ASC));
  

ALTER TABLE `vrjw534e3pgu7qdo`.`Transaction` 
ADD INDEX `food_id_idx` (`food_id` ASC);
;
ALTER TABLE `vrjw534e3pgu7qdo`.`Transaction` 
ADD CONSTRAINT `transanction_id`
  FOREIGN KEY (`transanction_id`)
  REFERENCES `vrjw534e3pgu7qdo`.`Survey` (`transanction_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `food_id`
  FOREIGN KEY (`food_id`)
  REFERENCES `vrjw534e3pgu7qdo`.`Food_Info` (`food_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;



SELECT * FROM vrjw534e3pgu7qdo.Food_Info;

INSERT INTO Food_Info(name,calorie,has_image,menu_price,material_cost,category)
VALUES('Gyoza',200,1,6.99,2.99,'Appetizers');

INSERT INTO Food_Info(name,calorie,has_image,menu_price,material_cost,category)
VALUES('Edamame',300,1,6.99,3.99,'Appetizers'),
        ('YAKITORI',400,0,4.99,2.99,'Appetizers'),
                ('SPRING ROLL',560,0,4.99,3.99,'Appetizers');
                
                

INSERT INTO Food_Info(name,calorie,has_image,menu_price,material_cost,category)
VALUES('HAKODATE',890,0,10.99,7.99,'Noodles'),
      ('SAPPORO',540,1,12.99,9.99,'Noodles'),
            ('KITAKATA',1200,1,12.99,7.99,'Noodles'),
            ('CHUKA SOBA',980,0,10.99,5.99,'Noodles'),
            ('TSUKEMEN',780,1,12.99,10.99,'Noodles'),
            ('TAKAYAMA',1300,0,10.99,8.99,'Noodles');


INSERT INTO Food_Info(name,calorie,has_image,menu_price,material_cost,category)
VALUES('CALIFORNIA ROLL',750,1,12.99,7.99,'Sushi'),
      ('SPIDER ROLL',640,0,10.99,9.99,'Sushi'),
            ('TUNA SUSHI',890,1,12.99,7.99,'Sushi'),
            ('DYNAMITE ROLL',780,0,10.99,5.99,'Sushi'),
            ('PHILADELPHIA ROLL',980,1,12.99,10.99,'Sushi'),
            ('SEATTLE ROLL',780,0,10.99,8.99,'Sushi');
            
            
INSERT INTO Food_Info(name,calorie,has_image,menu_price,material_cost,category)
VALUES('COKE',150,1,2.99,0.99,'Beverage'),
      ('BEER',99,1,4.99,2.99,'Beverage'),
            ('TEA',100,1,2.99,1.99,'Beverage');
            