#!/usr/bin/perl
use YAML::XS qw/LoadFile Dump DumpFile/;
$YAML::XS::DumpCode = 1;
$YAML::XS::LoadCode = 1;
use Data::Dumper;
my $yaml = LoadFile('spec/swagger.yaml');
#print Dumper($yaml);
foreach $key( keys %{$yaml} ) 
        { 
        print "$key\n";
        if ($key eq 'paths' or $key eq 'definitions')
                {
                foreach $key2 ( keys %{$yaml->{$key}} )
                        {
                        $key2path = "$key2.yaml";
                        $key2path =~ s/\//@/g;
                        $key2path =~ s/^@//g;
                        $key2path =~ s/@\.yaml/.yaml/g;
                        print "*** $key2 -> $key2path ***\n";
                        $a = Dump($yaml->{$key}->{$key2});
                        $a =~ s@: !!perl/scalar:main '@: ! '@g;
                        $a =~ s@- !!perl/scalar:main '@- ! '@g;
                        open (FILE,">spec/$key/$key2path");
                        print FILE $a;
                        close FILE;
                        }
                }
        }
