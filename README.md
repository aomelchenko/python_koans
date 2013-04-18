Installation and Getting Started
=============

First of all you should sign-up for a CloudMade API key, by following this [link][], if you have not done it before.

###To install run:

	gem install cloudmade.gem



Get tile from CloudMade Tile Server
=============

Class _TilesService_ allows you to get tile (image of map) from CloudMade Tile Server.

Lets request the tile that contains the point with latitude = 47.26117 longitude = 9.59882 with zoom_level = 10

<code>
	#Example usage of CloudMade's API

	require 'cloudmade'
	include CloudMade

	cm = Client.from_parameters('Your_API_Key')
	png = cm.tiles.get_tile(47.26117, 9.59882, 10)
	file = File.new('my_tile.png', 'w')
	file.write(png)
	file.close
<code>

Lets look at what each bit of code is doing here:

###1. First you should import CloudMade module
<code>
	require 'cloudmade'
	include CloudMade
<code>

The last line means you can use CloudMade module classes directly, without referencing the module name

###2. Setup connection
<code>
	cm = Client.from_parameters('Your_API_Key')
<code>
Your_API_Key - Replace this with your CloudMade API key

Client class allows you to communicate with different CloudMade services, like Geocoding, Tiles etc.

###3. Get tile
<code>
	png = cm.tiles.get_tile(47.26117, 9.59882, 10)
<code>

_get_tile_ is a TileService's method, which returns a tile image.

###4. Save tile into file
<code>
	file = File.new('my_tile.png', 'w')
	file.write(png)
	file.close
<code>
=======


[link]: http://account.cloudmade.com/register
