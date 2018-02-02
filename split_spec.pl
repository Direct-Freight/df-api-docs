#!/usr/bin/perl
use YAML::XS qw/LoadFile Dump DumpFile Load/;
use File::Slurp;
use Data::Dumper;
$YAML::XS::DumpCode = 1;
$YAML::XS::LoadCode = 1;
my $text = read_file('web_deploy/swagger.yaml') ;
my $yaml = Load($text); #read from combined one.
foreach my $key( keys %{$yaml} ) 
        { 
        if ($key eq 'paths' or $key eq 'definitions')
                {
                foreach my $key2 ( keys %{$yaml->{$key}} )
                        {
                        my $key2filename = "$key2.yaml";
                        $key2filename =~ s/\//@/g;
                        $key2filename =~ s/^@//g;
                        $key2filename =~ s/@\.yaml/.yaml/g;
                        my $out = Dump($yaml->{$key}->{$key2});
                        $out =~ s@: !!perl/scalar:main '@: ! '@g;
                        $out =~ s@- !!perl/scalar:main '@- ! '@g;
                        open (FILE,">spec/$key/$key2filename"); #write to the individual paths and definitions
                        print FILE $out;
                        close FILE;
                        }
                }
        }
my @lines = split("\n",$text);
open (FILE,">spec/swagger.yaml"); #write to the individual paths and definitions
foreach my $line (@lines)
        {       
        last if($line =~ /^(definitions|paths)/);
        chomp($line);
        print FILE "$line\n";
        }
close FILE;
