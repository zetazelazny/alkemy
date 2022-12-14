USE [master]
GO
/****** Object:  Database [prisma]    Script Date: 2/11/2022 12:14:41 ******/
CREATE DATABASE [prisma]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'prisma', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\prisma.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'prisma_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\prisma_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [prisma] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [prisma].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [prisma] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [prisma] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [prisma] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [prisma] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [prisma] SET ARITHABORT OFF 
GO
ALTER DATABASE [prisma] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [prisma] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [prisma] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [prisma] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [prisma] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [prisma] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [prisma] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [prisma] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [prisma] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [prisma] SET  ENABLE_BROKER 
GO
ALTER DATABASE [prisma] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [prisma] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [prisma] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [prisma] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [prisma] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [prisma] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [prisma] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [prisma] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [prisma] SET  MULTI_USER 
GO
ALTER DATABASE [prisma] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [prisma] SET DB_CHAINING OFF 
GO
ALTER DATABASE [prisma] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [prisma] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [prisma] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [prisma] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [prisma] SET QUERY_STORE = OFF
GO
USE [prisma]
GO
/****** Object:  Table [dbo].[Alumno]    Script Date: 2/11/2022 12:14:41 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Alumno](
	[Legajo] [int] NOT NULL,
	[Nombre] [varchar](50) NULL,
	[Apellido] [varchar](50) NULL,
	[Fec_Nacimiento] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[Legajo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cursa]    Script Date: 2/11/2022 12:14:41 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cursa](
	[Legajo] [int] NOT NULL,
	[ID_Materia] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Materia]    Script Date: 2/11/2022 12:14:41 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Materia](
	[ID_Materia] [int] IDENTITY(1,1) NOT NULL,
	[Descripcion] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_Materia] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fec_Nacimiento]) VALUES (1, N'Lionel', N'Messi', CAST(N'1987-06-24' AS Date))
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fec_Nacimiento]) VALUES (2, N'Rodrigo', N'De Paul', CAST(N'1994-05-24' AS Date))
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fec_Nacimiento]) VALUES (3, N'Lautaro', N'Martinez', CAST(N'1997-08-22' AS Date))
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fec_Nacimiento]) VALUES (4, N'Emiliano', N'Martinez', CAST(N'1992-09-02' AS Date))
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fec_Nacimiento]) VALUES (5, N'Marcos', N'Acuña', CAST(N'1991-10-28' AS Date))
GO
INSERT [dbo].[Cursa] ([Legajo], [ID_Materia]) VALUES (1, 2)
INSERT [dbo].[Cursa] ([Legajo], [ID_Materia]) VALUES (2, 1)
INSERT [dbo].[Cursa] ([Legajo], [ID_Materia]) VALUES (3, 3)
INSERT [dbo].[Cursa] ([Legajo], [ID_Materia]) VALUES (4, 4)
INSERT [dbo].[Cursa] ([Legajo], [ID_Materia]) VALUES (5, 5)
GO
SET IDENTITY_INSERT [dbo].[Materia] ON 

INSERT [dbo].[Materia] ([ID_Materia], [Descripcion]) VALUES (1, N'Jueguitos')
INSERT [dbo].[Materia] ([ID_Materia], [Descripcion]) VALUES (2, N'Tiros libres')
INSERT [dbo].[Materia] ([ID_Materia], [Descripcion]) VALUES (3, N'Penales')
INSERT [dbo].[Materia] ([ID_Materia], [Descripcion]) VALUES (4, N'Centros')
INSERT [dbo].[Materia] ([ID_Materia], [Descripcion]) VALUES (5, N'Baile')
SET IDENTITY_INSERT [dbo].[Materia] OFF
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD FOREIGN KEY([ID_Materia])
REFERENCES [dbo].[Materia] ([ID_Materia])
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD FOREIGN KEY([Legajo])
REFERENCES [dbo].[Alumno] ([Legajo])
GO
USE [master]
GO
ALTER DATABASE [prisma] SET  READ_WRITE 
GO
