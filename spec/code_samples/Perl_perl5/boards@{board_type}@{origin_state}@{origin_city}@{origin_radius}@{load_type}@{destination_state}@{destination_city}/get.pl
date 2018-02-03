#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new("GET",
"https://www.directfreight.com/api/boards/%7Bboard_type%7D/%7Borigin_state%7D/%7Borigin_city%7D/%7Borigin_radius%7D/%7Bload_type%7D/%7Bdestination_state%7D/%7Bdestination_city%7D");
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print Dumper($response->json_content);