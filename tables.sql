CREATE DATABASE depenses
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;

USE depenses;

CREATE TABLE `expenditure` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `amount` double NOT NULL,
  `date` datetime NOT NULL,
  `comment` text NOT NULL,
  `title` varchar(256) NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `team` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `from_user` int(11) NOT NULL,
  `to_user` int(11) NOT NULL,
  `amount` double NOT NULL,
  `comment` varchar(256) DEFAULT '',
  `date` datetime NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `users_by_teams` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE `expenditure`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `team_id` (`team_id`);

ALTER TABLE `team`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_transaction_user_id_from` (`from_user`),
  ADD KEY `fk_transaction_user_id_to` (`to_user`),
  ADD KEY `fk_transaction_team_id` (`team_id`);

ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `users_by_teams`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`team_id`),
  ADD KEY `fk_users_by_teams_team_id` (`team_id`);


ALTER TABLE `expenditure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `team`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `users_by_teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `expenditure`
  ADD CONSTRAINT `fk_expenditure_team_id` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`),
  ADD CONSTRAINT `fk_expenditure_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `transaction`
  ADD CONSTRAINT `fk_transaction_team_id` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`),
  ADD CONSTRAINT `fk_transaction_user_id_from` FOREIGN KEY (`from_user`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `fk_transaction_user_id_to` FOREIGN KEY (`to_user`) REFERENCES `user` (`id`);

ALTER TABLE `users_by_teams`
  ADD CONSTRAINT `fk_users_by_teams_team_id` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`),
  ADD CONSTRAINT `fk_users_by_teams_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

