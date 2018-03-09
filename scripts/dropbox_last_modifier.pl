#!/usr/bin/perl
use Modern::Perl;
use URI::Escape;
use LWP::UserAgent::JSON;             
use HTTP::Request::JSON;
use Data::Dumper;

    my $browser = LWP::UserAgent::JSON->new();
    my $request = HTTP::Request::JSON->new("POST","https://api.dropboxapi.com/2/files/get_metadata");
    $request->header( 'Content-Type' => "application/json" );
    $request->header( 'Authorization' => "Bearer GcRqOqPzW-YAAAAAAABP9_GuyfVM8V20Ygrh2k0UsJtAEI2klrctlqE1rYfcNTwA" );
    $request->content('{"path":"/directfreight/swagger20-with-extensions.yaml"}');
    my $response = $browser->request($request);
    my $modified_by = $response->json_content->{sharing_info}->{modified_by};
    $request = HTTP::Request::JSON->new("POST","https://api.dropboxapi.com/2/users/get_account");
    $request->header( 'Content-Type' => "application/json" );
    $request->header( 'Authorization' => "Bearer GcRqOqPzW-YAAAAAAABP9_GuyfVM8V20Ygrh2k0UsJtAEI2klrctlqE1rYfcNTwA" );
    my $content = "{\"account_id\":\"$modified_by\"}";
    $request->content($content);
    $response = $browser->request($request);
    my $email = $response->json_content->{email};
    my $display = $response->json_content->{name}->{display_name};
    print "$email:$display";    
