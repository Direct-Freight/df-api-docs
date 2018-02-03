#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(%s,
"PATCH") https://www.directfreight.com/api/postings/custom_categories/%7Bcategory_type%7D
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;