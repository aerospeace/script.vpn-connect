from subprocess import Popen, PIPE, check_output
import xbmc
import xbmcaddon
import xbmcgui

# Get addon info
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

# Get settings
connection_name = addon.getSetting('connection_name')
xbmc.log("Connection name use is " + connection_name)

connection_status_output = check_output('connmanctl services', shell=True)
xbmc.log("connection_status_output is " + str(connection_status_output))

# string_if_connected = f'* R WireGuard VPN Tunnel {connection_name}'
string_if_connected = '* R WireGuard VPN Tunnel ' + connection_name
xbmc.log("string_if_connected is " + string_if_connected)

connected = string_if_connected in connection_status_output
xbmc.log("connected is " + str(connected))

command = 'disconnect' if connected else 'connect'
xbmc.log("command is " + str(command))

proc = Popen(['connmanctl', command, connection_name], stdout=PIPE, stdin=PIPE, stderr=PIPE)

# xbmcgui.Dialog().notification(addonname, f"vpn {command}ed")
xbmcgui.Dialog().notification(addonname, "vpn " + command + "ed")
