-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2023 at 04:35 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `expertizcore`
--

-- --------------------------------------------------------

--
-- Table structure for table `agent`
--

CREATE TABLE `agent` (
  `IDAgent` int(11) NOT NULL,
  `CodeAgent` varchar(50) DEFAULT NULL,
  `msisdn` varchar(50) NOT NULL,
  `NomAgent` varchar(50) DEFAULT NULL,
  `AgentActif` tinyint(4) DEFAULT 0,
  `CodeOperateur` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `codebank`
--

CREATE TABLE `codebank` (
  `IDCodeBank` int(11) NOT NULL,
  `CodeBank` varchar(50) NOT NULL,
  `CodeSwift` varchar(50) DEFAULT NULL,
  `NomBank` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `comptes`
--

CREATE TABLE `comptes` (
  `IDComptes` int(11) NOT NULL,
  `Codeage` varchar(6) DEFAULT NULL,
  `ncp` varchar(15) DEFAULT NULL,
  `typ` varchar(7) DEFAULT NULL,
  `Solde` decimal(24,6) DEFAULT 0.000000,
  `CodeBank` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `evenements`
--

CREATE TABLE `evenements` (
  `IDevenements` bigint(20) NOT NULL,
  `montant` decimal(24,6) DEFAULT 0.000000,
  `refOrig` varchar(50) DEFAULT NULL,
  `natOrig` varchar(5) DEFAULT NULL,
  `DoOrig` varchar(50) DEFAULT NULL,
  `BenOrig` varchar(50) DEFAULT NULL,
  `refFin` varchar(50) DEFAULT NULL,
  `etaOrig` varchar(2) DEFAULT NULL,
  `userOrig` varchar(10) DEFAULT NULL,
  `Caisseorig` varchar(10) DEFAULT NULL,
  `chqOrig` varchar(50) DEFAULT NULL,
  `DoFin` varchar(50) DEFAULT NULL,
  `BenFIn` varchar(50) DEFAULT NULL,
  `sensOrig` varchar(1) DEFAULT NULL,
  `natFin` varchar(10) DEFAULT NULL,
  `dcoOrig` varchar(50) DEFAULT NULL,
  `hsaiOrig` varchar(50) DEFAULT NULL,
  `etaFin` varchar(5) DEFAULT NULL,
  `statutTrt` varchar(2) DEFAULT NULL,
  `statutCreation` varchar(10) DEFAULT NULL,
  `refMTN` varchar(50) DEFAULT NULL,
  `CodeOperateur` varchar(50) DEFAULT NULL,
  `Msisdn` varchar(50) DEFAULT NULL,
  `cptMTNSide` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `historique`
--

CREATE TABLE `historique` (
  `IDhistorique` bigint(20) NOT NULL,
  `montant` decimal(24,6) DEFAULT 0.000000,
  `refOrig` varchar(50) DEFAULT NULL,
  `natOrig` varchar(5) DEFAULT NULL,
  `DoOrig` varchar(50) DEFAULT NULL,
  `BenOrig` varchar(50) DEFAULT NULL,
  `refFin` varchar(50) DEFAULT NULL,
  `etaOrig` varchar(2) DEFAULT NULL,
  `userOrig` varchar(10) DEFAULT NULL,
  `Caisseorig` varchar(10) DEFAULT NULL,
  `chqOrig` varchar(50) DEFAULT NULL,
  `DoFin` varchar(50) DEFAULT NULL,
  `BenFIn` varchar(50) DEFAULT NULL,
  `sensOrig` varchar(1) DEFAULT NULL,
  `natFin` varchar(10) DEFAULT NULL,
  `dcoOrig` varchar(50) DEFAULT NULL,
  `hsaiOrig` varchar(50) DEFAULT NULL,
  `etaFin` varchar(5) DEFAULT NULL,
  `statutTrt` varchar(2) DEFAULT NULL,
  `statutCreation` varchar(10) DEFAULT NULL,
  `refMTN` varchar(50) DEFAULT NULL,
  `CodeOperateur` varchar(50) DEFAULT NULL,
  `Msisdn` varchar(50) DEFAULT NULL,
  `cptMTNSide` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `operateur`
--

CREATE TABLE `operateur` (
  `IDOperateur` int(11) NOT NULL,
  `CodeOperateur` varchar(50) NOT NULL,
  `DescriptionOP` varchar(50) DEFAULT NULL,
  `CodePays` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `operateur`
--

INSERT INTO `operateur` (`IDOperateur`, `CodeOperateur`, `DescriptionOP`, `CodePays`) VALUES
(1, 'MTN', 'Opérateur de Téléphonie MTN', 'BJ'),
(2, 'MOOV', 'Opérateur de Téléphonie MOOV', 'BJ');

-- --------------------------------------------------------

--
-- Table structure for table `pays`
--

CREATE TABLE `pays` (
  `IDPays` int(11) NOT NULL,
  `CodePays` varchar(5) NOT NULL,
  `LibPays` varchar(50) DEFAULT NULL,
  `indicatif` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pays`
--

INSERT INTO `pays` (`IDPays`, `CodePays`, `LibPays`, `indicatif`) VALUES
(1, 'BJ', 'BENIN', '229');

-- --------------------------------------------------------

--
-- Table structure for table `profil`
--

CREATE TABLE `profil` (
  `IDProfil` int(11) NOT NULL,
  `CodeProfil` varchar(50) NOT NULL,
  `DescriptionPro` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `profil`
--

INSERT INTO `profil` (`IDProfil`, `CodeProfil`, `DescriptionPro`) VALUES
(1, 'ADMIN', 'Administrateur'),
(2, 'CAISSIER', 'Opérateur de saisie Front office'),
(3, 'CONTROL', 'Chargé des habilitations'),
(4, 'BACK', 'Opérateur de saisie back-office');

-- --------------------------------------------------------

--
-- Table structure for table `sens`
--

CREATE TABLE `sens` (
  `IDSens` int(11) NOT NULL,
  `CodeSens` varchar(1) NOT NULL,
  `LibelleSens` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sens`
--

INSERT INTO `sens` (`IDSens`, `CodeSens`, `LibelleSens`) VALUES
(1, 'D', 'Débit'),
(2, 'C', 'Crédit');

-- --------------------------------------------------------

--
-- Table structure for table `typetransaction`
--

CREATE TABLE `typetransaction` (
  `IDTypeTransaction` int(11) NOT NULL,
  `CodeType` varchar(5) NOT NULL,
  `LibelleType` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `typetransaction`
--

INSERT INTO `typetransaction` (`IDTypeTransaction`, `CodeType`, `LibelleType`) VALUES
(1, 'VERSP', 'Versement Espèce'),
(2, 'VRT', 'Virement'),
(3, 'CHQ', 'Remise chèque'),
(4, 'RET', 'Retrait');

-- --------------------------------------------------------

--
-- Table structure for table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `IDUtilisateur` int(11) NOT NULL,
  `CodeUser` varchar(10) NOT NULL,
  `NomUser` varchar(50) DEFAULT NULL,
  `UserActif` tinyint(4) DEFAULT 0,
  `CodeProfil` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agent`
--
ALTER TABLE `agent`
  ADD PRIMARY KEY (`IDAgent`),
  ADD UNIQUE KEY `msisdn` (`msisdn`),
  ADD KEY `WDIDX_Agent_CodeOperateur` (`CodeOperateur`);

--
-- Indexes for table `codebank`
--
ALTER TABLE `codebank`
  ADD PRIMARY KEY (`IDCodeBank`),
  ADD UNIQUE KEY `CodeBank` (`CodeBank`);

--
-- Indexes for table `comptes`
--
ALTER TABLE `comptes`
  ADD PRIMARY KEY (`IDComptes`),
  ADD KEY `WDIDX_Comptes_CodeBank` (`CodeBank`);

--
-- Indexes for table `evenements`
--
ALTER TABLE `evenements`
  ADD PRIMARY KEY (`IDevenements`),
  ADD KEY `WDIDX_evenements_natOrig` (`natOrig`),
  ADD KEY `WDIDX_evenements_userOrig` (`userOrig`),
  ADD KEY `WDIDX_evenements_sensOrig` (`sensOrig`),
  ADD KEY `WDIDX_evenements_CodeOperateur` (`CodeOperateur`),
  ADD KEY `WDIDX_evenements_Msisdn` (`Msisdn`);

--
-- Indexes for table `historique`
--
ALTER TABLE `historique`
  ADD PRIMARY KEY (`IDhistorique`),
  ADD KEY `WDIDX_historique_natOrig` (`natOrig`),
  ADD KEY `WDIDX_historique_sensOrig` (`sensOrig`),
  ADD KEY `WDIDX_historique_CodeOperateur` (`CodeOperateur`),
  ADD KEY `WDIDX_historique_Msisdn` (`Msisdn`);

--
-- Indexes for table `operateur`
--
ALTER TABLE `operateur`
  ADD PRIMARY KEY (`IDOperateur`),
  ADD UNIQUE KEY `CodeOperateur` (`CodeOperateur`),
  ADD KEY `WDIDX_Operateur_CodePays` (`CodePays`);

--
-- Indexes for table `pays`
--
ALTER TABLE `pays`
  ADD PRIMARY KEY (`IDPays`),
  ADD UNIQUE KEY `CodePays` (`CodePays`);

--
-- Indexes for table `profil`
--
ALTER TABLE `profil`
  ADD PRIMARY KEY (`IDProfil`),
  ADD UNIQUE KEY `CodeProfil` (`CodeProfil`);

--
-- Indexes for table `sens`
--
ALTER TABLE `sens`
  ADD PRIMARY KEY (`IDSens`),
  ADD UNIQUE KEY `CodeSens` (`CodeSens`);

--
-- Indexes for table `typetransaction`
--
ALTER TABLE `typetransaction`
  ADD PRIMARY KEY (`IDTypeTransaction`),
  ADD UNIQUE KEY `CodeType` (`CodeType`);

--
-- Indexes for table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`IDUtilisateur`),
  ADD UNIQUE KEY `CodeUser` (`CodeUser`),
  ADD KEY `WDIDX_Utilisateur_CodeProfil` (`CodeProfil`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agent`
--
ALTER TABLE `agent`
  MODIFY `IDAgent` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `codebank`
--
ALTER TABLE `codebank`
  MODIFY `IDCodeBank` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `comptes`
--
ALTER TABLE `comptes`
  MODIFY `IDComptes` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `evenements`
--
ALTER TABLE `evenements`
  MODIFY `IDevenements` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `historique`
--
ALTER TABLE `historique`
  MODIFY `IDhistorique` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `operateur`
--
ALTER TABLE `operateur`
  MODIFY `IDOperateur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pays`
--
ALTER TABLE `pays`
  MODIFY `IDPays` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `profil`
--
ALTER TABLE `profil`
  MODIFY `IDProfil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `sens`
--
ALTER TABLE `sens`
  MODIFY `IDSens` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `typetransaction`
--
ALTER TABLE `typetransaction`
  MODIFY `IDTypeTransaction` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `utilisateur`
--
ALTER TABLE `utilisateur`
  MODIFY `IDUtilisateur` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `agent`
--
ALTER TABLE `agent`
  ADD CONSTRAINT `agent_ibfk_1` FOREIGN KEY (`CodeOperateur`) REFERENCES `operateur` (`CodeOperateur`);

--
-- Constraints for table `comptes`
--
ALTER TABLE `comptes`
  ADD CONSTRAINT `comptes_ibfk_1` FOREIGN KEY (`CodeBank`) REFERENCES `codebank` (`CodeBank`);

--
-- Constraints for table `evenements`
--
ALTER TABLE `evenements`
  ADD CONSTRAINT `evenements_ibfk_1` FOREIGN KEY (`CodeOperateur`) REFERENCES `operateur` (`CodeOperateur`),
  ADD CONSTRAINT `evenements_ibfk_2` FOREIGN KEY (`Msisdn`) REFERENCES `agent` (`msisdn`),
  ADD CONSTRAINT `evenements_ibfk_3` FOREIGN KEY (`natOrig`) REFERENCES `typetransaction` (`CodeType`),
  ADD CONSTRAINT `evenements_ibfk_4` FOREIGN KEY (`sensOrig`) REFERENCES `sens` (`CodeSens`),
  ADD CONSTRAINT `evenements_ibfk_5` FOREIGN KEY (`userOrig`) REFERENCES `utilisateur` (`CodeUser`);

--
-- Constraints for table `operateur`
--
ALTER TABLE `operateur`
  ADD CONSTRAINT `operateur_ibfk_1` FOREIGN KEY (`CodePays`) REFERENCES `pays` (`CodePays`);

--
-- Constraints for table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD CONSTRAINT `utilisateur_ibfk_1` FOREIGN KEY (`CodeProfil`) REFERENCES `profil` (`CodeProfil`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
