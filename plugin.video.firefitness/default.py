#------------------------------------------------------------#
# -*- coding: utf-8 -*-                                      #
#------------------------------------------------------------#
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)    #
# Based on code from youtube addon                           #
#                                                            #
# Author: Fire TV GURU <> Thx for the code Pulse             #
#------------------------------------------------------------#

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.firefitness'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1  = "FitnessBlender"
YOUTUBE_CHANNEL_ID_2  = "robinforlife"
YOUTUBE_CHANNEL_ID_3  = "myfitgirls"
YOUTUBE_CHANNEL_ID_4  = "lovezumba"
YOUTUBE_CHANNEL_ID_5  = "BeFit"
YOUTUBE_CHANNEL_ID_6  = "runtasticFitness"
YOUTUBE_CHANNEL_ID_7  = "Perfectfitnesstv"
YOUTUBE_CHANNEL_ID_8  = "popsugartvfit"
YOUTUBE_CHANNEL_ID_9  = "bodybuildandfitness"
YOUTUBE_CHANNEL_ID_10 = "superherofitnesstv"
YOUTUBE_CHANNEL_ID_11 = "STORYOFSHIRTLESS"
YOUTUBE_CHANNEL_ID_12 = "TheQuestForFitness"
YOUTUBE_CHANNEL_ID_13 = "fit"
YOUTUBE_CHANNEL_ID_14 = "buffdudes"
YOUTUBE_CHANNEL_ID_15 = "yogawithadriene"
YOUTUBE_CHANNEL_ID_16 = "ZuzkaLight"
YOUTUBE_CHANNEL_ID_17 = "psychetruth"
YOUTUBE_CHANNEL_ID_18 = "UCKrd5VRxcXFvMf4-9VmpLuA"
YOUTUBE_CHANNEL_ID_19 = "UCPNmIJvkpnyKa_BMLwUaJpw"
YOUTUBE_CHANNEL_ID_20 = "OfficialBarstarzz"
YOUTUBE_CHANNEL_ID_21 = "TheMiamiTrainer"
YOUTUBE_CHANNEL_ID_22 = "lesleyfightmaster"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Fitness Blender",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i.imgur.com/wC9SNkN.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="robinforlife",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://i.imgur.com/f8mB1TS.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="My Fitness Girls",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://i.imgur.com/RkoghOn.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Zumba Fitness",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://i.imgur.com/cpVqHvZ.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Be Fit",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://i.imgur.com/Nq4RRnD.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Runtastic Fitness",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-8HwQbazlHEE/AAAAAAAAAAI/AAAAAAAAAAA/xR6JpICwpuk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Perfect fitness tv",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-xc9T8yyhtjU/AAAAAAAAAAI/AAAAAAAAAAA/X8LdarAC9Zs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="pop sugar tvfit",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-BsrLTcw7rsg/AAAAAAAAAAI/AAAAAAAAAAA/e7g-a22BudQ/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="bodybuild and fitness",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-NBMHkKE2DAo/AAAAAAAAAAI/AAAAAAAAAAA/6as3xyn-PK8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="super hero fitness tv",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-s_xWWsIqWKo/AAAAAAAAAAI/AAAAAAAAAAA/btf7fYzKTYk/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Fit Media Channel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-03wsplj7Lys/AAAAAAAAAAI/AAAAAAAAAAA/gSOa141K-ZI/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Jon Venus",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-pie-pRJV8Uo/AAAAAAAAAAI/AAAAAAAAAAA/mZhDbjbAP6g/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="FiT – Global Fitness Network",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-ScLdVt6iA7Q/AAAAAAAAAAI/AAAAAAAAAAA/LaaRVR015gk/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Buff Dudes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-kzRmDxQlTXE/AAAAAAAAAAI/AAAAAAAAAAA/AdPSu20tFkY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Yoga With Adriene",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://i.imgur.com/ZDBe1C7.jpg",
        folder=True ) 	
		
    plugintools.add_item( 
        #action="", 
        title="Zuzka Light",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-1YXoeQnh-2c/AAAAAAAAAAI/AAAAAAAAAAA/XW_6bCMzdrU/s100-c-k-no/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Psyche Truth",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-JgiXLOMFYz0/AAAAAAAAAAI/AAAAAAAAAAA/Gd_X8gBDC-4/s100-c-k-no/photo.jpg",
        folder=True ) 		
		
    plugintools.add_item( 
        #action="", 
        title="Brendan Meyers",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-svKJS_bYl-0/AAAAAAAAAAI/AAAAAAAAAAA/4TrvFpAYg8s/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True ) 		
		
    plugintools.add_item( 
        #action="", 
        title="Workout Videos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-oGZ5Qn1hPsc/AAAAAAAAAAI/AAAAAAAAAAA/aq5a0JfS1QM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Official Barstarzz",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-AaOjv-xzf1k/AAAAAAAAAAI/AAAAAAAAAAA/bBZs9Svl25I/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="The Miami Trainer",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-HZKBSpTN7SQ/AAAAAAAAAAI/AAAAAAAAAAA/3w3zf9pYhAU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Fightmaster Yoga",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-pnKh0WkTUfQ/AAAAAAAAAAI/AAAAAAAAAAA/2JTCHYaJiUw/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		
           
   	
run()
