#!/usr/bin/perl
use Modern::Perl;

while(<>)
        {
        my $line = $_;
        #sed -i "s/example: [\"']\(\[.*\]\)[\"']$/example: \1/g" $APIDOCS_PATH/swagger20-with-extensions.yaml #remove extra quotes from examples
        if($line =~ /example: ["']\[.*\]["']/)
                {
                $line =~ s/example: ["']\[/example: \[/g;
                $line =~ s/\]["']/\]/g;
                $line =~ s/\\"/"/g;
                print $line;
                }
        else { print "$line"; }
        }
