# Run by the startup file net.siriserver.plist or .bash_profile with
# function juizServer { cd $SIRIREPOSITORY/SiriServerCore/startup; ./juizServer.sh; }

sudo systemsetup -setremotelogin on
cd ../
sudo python SiriServer.py -p 443 -l debug