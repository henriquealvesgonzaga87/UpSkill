from Classe_Python_MySQL_Estrutura_Dados import *

bd = Classe_Python_MySQL_Estrutura_Dados(servidor='localhost',
                                         utilizador='root',
                                         password='root',
                                         base_dados='sakila')
bd.ListTables()
bd.ListTablesAndStructure()
# bd.ListTablesData()


# List of tables --------------------
# Table  ('actor',)
# Table  ('address',)
# Table  ('category',)
# Table  ('city',)
# Table  ('country',)
# Table  ('customer',)
# Table  ('film',)
# Table  ('film_actor',)
# Table  ('film_category',)
# Table  ('film_text',)
# Table  ('inventory',)
# Table  ('language',)
# Table  ('no_charset',)
# Table  ('payment',)
# Table  ('rental',)
# Table  ('staff',)
# Table  ('store',)
# List of tables --------------------
# Table  ('actor',)
# Tabela --------------------actor
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('actor_id', 'smallint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('first_name', 'varchar(45)', 'NO', '', None, '')
# ('last_name', 'varchar(45)', 'NO', 'MUL', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('address',)
# Tabela --------------------address
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('address_id', 'smallint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('address', 'varchar(50)', 'NO', '', None, '')
# ('address2', 'varchar(50)', 'YES', '', None, '')
# ('district', 'varchar(20)', 'NO', '', None, '')
# ('city_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('postal_code', 'varchar(10)', 'YES', '', None, '')
# ('phone', 'varchar(20)', 'NO', '', None, '')
# ('location', 'geometry', 'NO', 'MUL', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('category',)
# Tabela --------------------category
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('category_id', 'tinyint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('name', 'varchar(25)', 'NO', '', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('city',)
# Tabela --------------------city
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('city_id', 'smallint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('city', 'varchar(50)', 'NO', '', None, '')
# ('country_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('country',)
# Tabela --------------------country
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('country_id', 'smallint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('country', 'varchar(50)', 'NO', '', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('customer',)
# Tabela --------------------customer
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('customer_id', 'smallint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('store_id', 'tinyint unsigned', 'NO', 'MUL', None, '')
# ('first_name', 'varchar(45)', 'NO', '', None, '')
# ('last_name', 'varchar(45)', 'NO', 'MUL', None, '')
# ('email', 'varchar(50)', 'YES', '', None, '')
# ('address_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('active', 'tinyint(1)', 'NO', '', '1', '')
# ('create_date', 'datetime', 'NO', '', None, '')
# ('last_update', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('film',)
# Tabela --------------------film
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('film_id', 'smallint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('title', 'varchar(128)', 'NO', 'MUL', None, '')
# ('description', 'text', 'YES', '', None, '')
# ('release_year', 'year', 'YES', '', None, '')
# ('language_id', 'tinyint unsigned', 'NO', 'MUL', None, '')
# ('original_language_id', 'tinyint unsigned', 'YES', 'MUL', None, '')
# ('rental_duration', 'tinyint unsigned', 'NO', '', '3', '')
# ('rental_rate', 'decimal(4,2)', 'NO', '', '4.99', '')
# ('length', 'smallint unsigned', 'YES', '', None, '')
# ('replacement_cost', 'decimal(5,2)', 'NO', '', '19.99', '')
# ('rating', "enum('G','PG','PG-13','R','NC-17')", 'YES', '', 'G', '')
# ('special_features', "set('Trailers','Commentaries','Deleted Scenes','Behind the Scenes')", 'YES', '', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('film_actor',)
# Tabela --------------------film_actor
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('actor_id', 'smallint unsigned', 'NO', 'PRI', None, '')
# ('film_id', 'smallint unsigned', 'NO', 'PRI', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('film_category',)
# Tabela --------------------film_category
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('film_id', 'smallint unsigned', 'NO', 'PRI', None, '')
# ('category_id', 'tinyint unsigned', 'NO', 'PRI', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('film_text',)
# Tabela --------------------film_text
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('film_id', 'smallint', 'NO', 'PRI', None, '')
# ('title', 'varchar(255)', 'NO', 'MUL', None, '')
# ('description', 'text', 'YES', '', None, '')
# Table  ('inventory',)
# Tabela --------------------inventory
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('inventory_id', 'mediumint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('film_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('store_id', 'tinyint unsigned', 'NO', 'MUL', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('language',)
# Tabela --------------------language
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('language_id', 'tinyint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('name', 'char(20)', 'NO', '', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('no_charset',)
# Tabela --------------------no_charset
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('my_column', 'varchar(255)', 'YES', '', None, '')
# Table  ('payment',)
# Tabela --------------------payment
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('payment_id', 'smallint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('customer_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('staff_id', 'tinyint unsigned', 'NO', 'MUL', None, '')
# ('rental_id', 'int', 'YES', 'MUL', None, '')
# ('amount', 'decimal(5,2)', 'NO', '', None, '')
# ('payment_date', 'datetime', 'NO', '', None, '')
# ('last_update', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('rental',)
# Tabela --------------------rental
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('rental_id', 'int', 'NO', 'PRI', None, 'auto_increment')
# ('rental_date', 'datetime', 'NO', 'MUL', None, '')
# ('inventory_id', 'mediumint unsigned', 'NO', 'MUL', None, '')
# ('customer_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('return_date', 'datetime', 'YES', '', None, '')
# ('staff_id', 'tinyint unsigned', 'NO', 'MUL', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('staff',)
# Tabela --------------------staff
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('staff_id', 'tinyint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('first_name', 'varchar(45)', 'NO', '', None, '')
# ('last_name', 'varchar(45)', 'NO', '', None, '')
# ('address_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('picture', 'blob', 'YES', '', None, '')
# ('email', 'varchar(50)', 'YES', '', None, '')
# ('store_id', 'tinyint unsigned', 'NO', 'MUL', None, '')
# ('active', 'tinyint(1)', 'NO', '', '1', '')
# ('username', 'varchar(16)', 'NO', '', None, '')
# ('password', 'varchar(40)', 'YES', '', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
# Table  ('store',)
# Tabela --------------------store
# ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
# ('store_id', 'tinyint unsigned', 'NO', 'PRI', None, 'auto_increment')
# ('manager_staff_id', 'tinyint unsigned', 'NO', 'UNI', None, '')
# ('address_id', 'smallint unsigned', 'NO', 'MUL', None, '')
# ('last_update', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')