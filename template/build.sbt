// project 

name := "{name}"

version := "{version}"

organization := "{organization}"

scalaVersion := "{scala_version}"


// Dependencies 
resolvers ++= Seq("snapshots-repo" at "http://scala-tools.org/repo-snapshots")

libraryDependencies <<= scalaVersion {{ scalaversion => Seq(
  "junit" % "junit" % "4.7" % "optional")}}

// Compilation 
javacOptions ++= Seq()

javaOptions += "-Xmx2G"

scalacOptions ++= Seq("-deprecation", "-unchecked")

maxErrors := 20

pollInterval := 1000

logBuffered := false

cancelable := true