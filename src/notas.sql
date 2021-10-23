SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `courses`;
DROP TABLE IF EXISTS `activities`;
DROP TABLE IF EXISTS `roles`;
DROP TABLE IF EXISTS `comments`;
DROP TABLE IF EXISTS `users_courses`;
DROP TABLE IF EXISTS `users_activities`;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `users` (
    `user_id` INTEGER NOT NULL,
    `user_name` VARCHAR NOT NULL,
    `user_lastname` VARCHAR NOT NULL,
    `user_role` INTEGER NOT NULL,
    `user_dateborn` DATETIME NOT NULL,
    `user_email` VARCHAR NOT NULL,
    `user_phone` NUMERIC NOT NULL,
    `user_password` VARCHAR NOT NULL,
    `user_active` BOOLEAN NOT NULL,
    `create_at` TIMESTAMP NOT NULL,
    PRIMARY KEY (`user_id`),
    UNIQUE (`user_id`)
);

CREATE TABLE `courses` (
    `course_id` INTEGER NOT NULL,
    `course_name` VARCHAR NOT NULL,
    `course_description` TEXT NOT NULL,
    `course_schedule` DATETIME NOT NULL,
    `course_limit` INTEGER NOT NULL,
    PRIMARY KEY (`course_id`),
    UNIQUE (`course_id`)
);

CREATE TABLE `activities` (
    `activity_id` INTEGER NOT NULL,
    `activity_course` INTEGER NOT NULL,
    `activity_name` VARCHAR NOT NULL,
    `activity_description` TEXT NOT NULL,
    `activity_deadline` DATETIME NOT NULL,
    `activity_note` FLOAT NOT NULL,
    PRIMARY KEY (`activity_id`),
    UNIQUE (`activity_id`)
);

CREATE TABLE `roles` (
    `role_id` INTEGER NOT NULL,
    `role_name` VARCHAR NOT NULL,
    PRIMARY KEY (`role_id`),
    UNIQUE (`role_id`)
);

CREATE TABLE `comments` (
    `comment_id` INTEGER NOT NULL,
    `comment_body` TEXT NOT NULL,
    `comment_user` INTEGER NOT NULL,
    `comment_activity` INTEGER NOT NULL,
    `comment_to` INTEGER NOT NULL,
    PRIMARY KEY (`comment_id`),
    UNIQUE (`comment_id`)
);

CREATE TABLE `users_courses` (
    `id` INTEGER NOT NULL,
    `user_id` INTEGER NOT NULL,
    `course_id` INTEGER NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`id`)
);

CREATE TABLE `users_activities` (
    `id` INTEGER NOT NULL,
    `user_id` INTEGER NOT NULL,
    `activity_id` INTEGER NOT NULL,
    `activity_send` TIMESTAMP NOT NULL,
    `activity_note` FLOAT NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`id`)
);

ALTER TABLE `users` ADD FOREIGN KEY (`user_role`) REFERENCES `roles`(`role_id`);
ALTER TABLE `activities` ADD FOREIGN KEY (`activity_course`) REFERENCES `courses`(`course_id`);
ALTER TABLE `comments` ADD FOREIGN KEY (`comment_user`) REFERENCES `users`(`user_id`);
ALTER TABLE `users_courses` ADD FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`);
ALTER TABLE `users_courses` ADD FOREIGN KEY (`course_id`) REFERENCES `courses`(`course_id`);
ALTER TABLE `users_activities` ADD FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`);
ALTER TABLE `users_activities` ADD FOREIGN KEY (`activity_id`) REFERENCES `activities`(`activity_id`);