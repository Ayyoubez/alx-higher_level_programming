#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2]) || args[2] == null)
{
	console.log("Missing size");
} else {
	for (let i = 0; i < args[2]; i++)
	{
			console.log("X".repeat(args[2]));
	}}


