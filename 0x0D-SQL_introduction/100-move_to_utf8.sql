-- script that converts hbtn_0c_0 database to UTF8 in your MySQL server.
-- converts database to utf8mb4 collate
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts table to utf8
ALTER TABLE hbtn_0c_0.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts a field in a table to utf8
ALTER TABLE hbtn_0c_0.first_table MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
