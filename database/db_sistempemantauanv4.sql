-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 18 Jul 2017 pada 06.59
-- Versi Server: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `db_sistempemantauanv4`
--
CREATE DATABASE IF NOT EXISTS `db_sistempemantauanv4` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_sistempemantauanv4`;

-- --------------------------------------------------------

--
-- Struktur dari tabel `history`
--
-- Pembuatan: 05 Jun 2017 pada 21.08
--

DROP TABLE IF EXISTS `history`;
CREATE TABLE IF NOT EXISTS `history` (
  `id_rfid` varchar(12) NOT NULL,
  `no_ka` varchar(4) NOT NULL,
  `nama_ka` varchar(50) NOT NULL,
  `is_stasiun` varchar(5) NOT NULL,
  `nama_lokasi` varchar(50) NOT NULL,
  `gmaps_ls` varchar(10) DEFAULT NULL,
  `gmaps_bt` varchar(10) DEFAULT NULL,
  `real_ls` varchar(12) DEFAULT NULL,
  `real_bt` varchar(12) DEFAULT NULL,
  `kota_kab` varchar(50) DEFAULT NULL,
  `provinsi` varchar(50) DEFAULT NULL,
  `jalur` varchar(10) DEFAULT NULL,
  `waktu` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `history`
--

INSERT INTO `history` (`id_rfid`, `no_ka`, `nama_ka`, `is_stasiun`, `nama_lokasi`, `gmaps_ls`, `gmaps_bt`, `real_ls`, `real_bt`, `kota_kab`, `provinsi`, `jalur`, `waktu`) VALUES
('0010754885', '101', 'Malioboro Ekspress', 'TIDAK', 'Stasiun A (1,5km) - Stasiun B (1,5km)', '7,8005', '112,8005', '7`50.5 LS', '112`50.5 BT', 'Kota Malang', 'Jawa Timur', '', 'Mon Jul 10 10:01:06 2017');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pantau`
--
-- Pembuatan: 05 Jun 2017 pada 21.08
--

DROP TABLE IF EXISTS `pantau`;
CREATE TABLE IF NOT EXISTS `pantau` (
  `id_rfid` varchar(12) NOT NULL,
  `is_stasiun` varchar(5) NOT NULL,
  `nama_lokasi` varchar(60) NOT NULL,
  `gmaps_ls` varchar(10) DEFAULT NULL,
  `gmaps_bt` varchar(10) DEFAULT NULL,
  `real_ls` varchar(12) DEFAULT NULL,
  `real_bt` varchar(12) DEFAULT NULL,
  `kota_kab` varchar(50) DEFAULT NULL,
  `provinsi` varchar(50) DEFAULT NULL,
  `jalur` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pantau`
--

INSERT INTO `pantau` (`id_rfid`, `is_stasiun`, `nama_lokasi`, `gmaps_ls`, `gmaps_bt`, `real_ls`, `real_bt`, `kota_kab`, `provinsi`, `jalur`) VALUES
('0030188102', 'YA', 'Stasiun A - 1001', '7,2001', '112,2001', '7`15.5 LS', '112`15.5 BT', 'Kota Malang', 'Jawa Timur', 'Jalur 1'),
('0030076629', 'YA', 'Stasiun A - 1001', '7,2001', '112,2001', '7`15.5 LS', '112`15.5 BT', 'Kota Malang', 'Jawa Timur', 'Jalur 2'),
('0030154907', 'YA', 'Stasiun B - 1002', '8,3002', '113,3002', '8`16.5 LS', '113`16.5 BT', 'Kabupaten Pasuruan', 'Jawa Timur', 'Jalur 1'),
('0010755077', 'YA', 'Stasiun B - 1002', '8,3002', '113,3002', '8`16.5 LS', '113`16.5 BT', 'Kabupaten Pasuruan', 'Jawa Timur', 'Jalur 2'),
('0030096062', 'TIDAK', 'Stasiun A (1km) - Stasiun B (2km)', '7,5005', '112,5005', '7`25.5 LS', '112`25.5 BT', 'Kota Malang', 'Jawa Timur', 'In Out'),
('0010754885', 'TIDAK', 'Stasiun A (1,5km) - Stasiun B (1,5km)', '7,8005', '112,8005', '7`50.5 LS', '112`50.5 BT', 'Kota Malang', 'Jawa Timur', ''),
('0010806270', 'TIDAK', 'Stasiun A (2km) - Stasiun B (1km)', '8,0005', '113,0005', '8`00.5 LS', '113`00.5 BT', 'Kabupaten Pasuruan', 'Jawa Timur', 'In Out'),
('0010801890', 'TIDAK', 'Stasiun A (4km) - Stasiun B (1km)', '8,2505', '113,2505', '8`15.5 LS', '113`15.5 BT', 'Kabupaten Pasuruan', 'Jawa Timur', 'In Out'),
('0005463952', 'TIDAK', 'Stasiun A (3km) - Stasiun B (2km)', '8,4505', '113,4505', '8`20.5 LS', '113`20.5 BT', 'Kabupaten Pasuruan', 'Jawa Timur', ''),
('0030179362', 'TIDAK', 'Stasiun A (2km) - Stasiun B (3km)', '7,4505', '112,4505', '7`20.5 LS', '112`20.5 BT', 'Kota Malang', 'Jawa Timur', ''),
('0005476080', 'TIDAK', 'Stasiun A (1km) - Stasiun B (4km)', '7,6505', '112,6505', '7`60.5 LS', '112`60.5 BT', 'Kota Malang', 'Jawa Timur', 'In Out');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
