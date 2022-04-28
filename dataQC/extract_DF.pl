#!/usr/bin/perl


my $input= $ARGV[0];


open(I,$input);

my @want;
my $line=0;
my @array;
while(<I>){
        if($line == 0){
                $i=$_;
                chomp($i);
                @array = split(",",$i);
                for (my $i=0 ; $i<$#array+1; $i++){
                        if($array[$i] =~ /^"21001./ or $array[$i] =~ /^"1558./ or $array[$i] =~ /^"1200./ or $array[$i] =~ /^"22040./ or $array[$i] =~ /^"1070./ or $array[$i] =~ /^"189./ or $array[$i] =~ /^"20127./) {
                                print $array[$i],"\t";
                                push (@want,$i);
                        }
                }
                print "\n";
        }else{
                $i=$_;
                chomp($i);
                @array = split(",",$i);
                for my $j(@want){
                        print $array[$j],"\t",;
                }
                print "\n";
        }
        $line = $line +1;
}close I;
