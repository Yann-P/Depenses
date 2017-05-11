SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `depenses`
--

-- --------------------------------------------------------

--
-- Table structure for table `expenditure`
--

CREATE TABLE `expenditure` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `amount` double NOT NULL,
  `date` datetime NOT NULL,
  `comment` text NOT NULL,
  `title` varchar(256) NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `team`
--

CREATE TABLE `team` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `from_user` int(11) NOT NULL,
  `to_user` int(11) NOT NULL,
  `amount` double NOT NULL,
  `comment` varchar(256) DEFAULT '',
  `date` datetime NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users_by_teams`
--

CREATE TABLE `users_by_teams` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `expenditure`
--
ALTER TABLE `expenditure`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `team_id` (`team_id`);

--
-- Indexes for table `team`
--
ALTER TABLE `team`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_transaction_user_id_from` (`from_user`),
  ADD KEY `fk_transaction_user_id_to` (`to_user`),
  ADD KEY `fk_transaction_team_id` (`team_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_by_teams`
--
ALTER TABLE `users_by_teams`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`team_id`),
  ADD KEY `fk_users_by_teams_team_id` (`team_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `expenditure`
--
ALTER TABLE `expenditure`
  ADD CONSTRAINT `fk_expenditure_team_id` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`),
  ADD CONSTRAINT `fk_expenditure_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `fk_transaction_team_id` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`),
  ADD CONSTRAINT `fk_transaction_user_id_from` FOREIGN KEY (`from_user`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `fk_transaction_user_id_to` FOREIGN KEY (`to_user`) REFERENCES `user` (`id`);

--
-- Constraints for table `users_by_teams`
--
ALTER TABLE `users_by_teams`
  ADD CONSTRAINT `fk_users_by_teams_team_id` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`),
  ADD CONSTRAINT `fk_users_by_teams_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
