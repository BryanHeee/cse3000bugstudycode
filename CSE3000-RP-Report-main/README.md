# CSE3000-RP-Report
CSE3000 Research Project data analysis script.

#### Requirements

| Name | Link |
|---|---|
| Python 3.7+ | [Pyhton Download and install](https://www.python.org/downloads/) |
| PyCharm IDE (recommended) | [PyCharm installation](https://www.jetbrains.com/pycharm/download/) |
| MySQL | [MySQL download and install](https://www.mysql.com/downloads/) |
| MySQL WorkBench (recommended) | [MySQL WorkBench download and install](https://dev.mysql.com/downloads/workbench/) |

## Setup the Database

To use the scripts we first need to setup the database:
``` 
-- Create the database

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cse3000`
--
CREATE DATABASE IF NOT EXISTS `cse3000` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `cse3000`;

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `id` int(11) NOT NULL,
  `issue_id` int(11) NOT NULL,
  `title` text,
  `url` text,
  `created_at` varchar(100) NOT NULL,
  `number` int(11) NOT NULL,
  `body` text,
  `closed_at` varchar(100) DEFAULT NULL,
  `comments` int(11) DEFAULT NULL,
  `comments_url` text,
  `labels` text,
  `pull_request` text,
  `state` varchar(100) DEFAULT NULL,
  `commits` int(11) DEFAULT NULL,
  `additions` int(11) DEFAULT NULL,
  `deletions` int(11) DEFAULT NULL,
  `changed_files` int(11) DEFAULT NULL,
  `commits_data` text,
  `updated_at` varchar(100) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pull_request`
--

CREATE TABLE `pull_request` (
  `id` int(11) NOT NULL,
  `pull_request_id` int(11) NOT NULL,
  `title` text,
  `url` text,
  `created_at` varchar(100) NOT NULL,
  `number` int(11) NOT NULL,
  `body` text,
  `closed_at` varchar(100) DEFAULT NULL,
  `comments` int(11) DEFAULT NULL,
  `comments_url` text,
  `labels` text,
  `pull_request` text,
  `state` varchar(100) DEFAULT NULL,
  `commits` int(11) DEFAULT NULL,
  `additions` int(11) DEFAULT NULL,
  `deletions` int(11) DEFAULT NULL,
  `changed_files` int(11) DEFAULT NULL,
  `commits_data` text,
  `updated_at` varchar(100) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `issue`
--
ALTER TABLE `issue`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `issue_id` (`issue_id`);

--
-- Indexes for table `pull_request`
--
ALTER TABLE `pull_request`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `issue_id` (`pull_request_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `issue`
--
ALTER TABLE `issue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pull_request`
--
ALTER TABLE `pull_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
```

You can save te script into a ".sql" file and import it directly into your MySQL. 

## Run the scripts

#### Clone

Clone this repo to your local machine using 
```
https://github.com/MattiaBonfanti-CS/CSE3000-RP-Report.git
```

#### Create Virtual Environment (venv)
Move to  the application folder and run in your terminal:
```
# Create virtualenv, make sure to use python3
$ virtualenv -p python3 venv
# Activate venv
$ source venv/bin/activate
```
Alternatively:
* Open the project with PyCharm (either Pro or CE)  or your favorite Python IDE
* Select python3 as project interpreter

## Setup local environment variables
Create a ".env" file in the root folder of the project with the following variables:
```
GITHUB_REPO=owner/name
GITHUB_TOKEN=your_token
MYSQL_HOST=your_mysql_host_address
MYSQL_DB=cse3000
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
START_YEAR=starting_year
START_MONTH=starting_month
START_DAY=starting_day
START_HOUR=starting_hour
START_MINUTES=starting_minutes
```

IMPORTANT: The "START_..." fields are used to set the starting date from which the data from GitHub is pulled. Keep in mind that the amount of requests to the GitHub API will run out periodically. Therefore make sure to update these values to the "updated_at" of the latest added item in the database before running the script again.

#### Install Requirements
Move to  the application folder and run in your terminal:
```
pip install -r requirements.txt
```

#### Run
Move to the "app" folder in the project and run in your terminal:
```
# Find and store issues to the database
python main.py
# or
python main.py issue

# Find and store pull_requests to the database
python main.py pull_request
```  

## Notes  
- You should keep the .gitignore updated file to make sure that any OS-specific and IDE-specific files do not get pushed to the repo (e.g. .idea).  
