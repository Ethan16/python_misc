<?php
function append_response()
{
    $req_flag = "Resp_";
    $req_var  = apache_request_headers();

    foreach($req_var as $key=>$value)
    {
	$find = strstr($key,$req_flag);
	if($find == FALSE || $find != $key)
	{
	   $new_key="req_".$key;
           header("$new_key:$value");
	}
        else
        {
           $new_key=substr_replace($key,"",0,strlen($req_flag));
	   header("$new_key:$value");
        }
   }
}
function append_response_server()
{
    $server_var  = $_SERVER;
    $reqURI = $server_var['REQUEST_URI'];
    header("REQURI:$reqURI");
    $clientIP = $server_var['REMOTE_ADDR'].":".$server_var['REMOTE_PORT'];
    header("CLIENTIPPORT:$clientIP");
    $serverIP = $server_var['SERVER_ADDR'].":".$server_var['SERVER_PORT'];
    header("SERVERIPPORT:$serverIP");
    $cacheFlag = $server_var['REQUEST_TIME'];;
    header("CACHEFLAG:$cacheFlag");
}
function gzip_out_put_file($filepath)
{
    $handle      = fopen($filepath, "r");
    $contents    = fread($handle, filesize ($filepath));
	
    $req_header  = apache_response_headers();
    $req_var = "normal";
	
    foreach($req_header as $key=>$value)
    {
        if(strcasecmp($key,"Content-Encoding")==0)
        {
            $req_var = trim($value);
            break;
        }		   
    } 
	
    if($req_var == "gzip")
    {
	$gstr = gzencode($contents);
        $md5file = md5($contents);
	header("FILEMD5:$md5file");
	header("Content-Encoding:gzip");
	echo $gstr;
	fclose($handle);
        return;
     }
    if($req_var == "deflate")
     {
	$gstr = gzdeflate($contents);
	$md5file = md5($contents);
	header("FILEMD5:$md5file");
	header("Content-Encoding:deflate");
	echo $gstr;
	fclose($handle);
	return;
     }
     if($req_var == "compress")
     {
        $gstr = gzcompress($contents);
        $md5file = md5($contents);
        header("FILEMD5:$md5file");
        header("Content-Encoding:compress");
        echo $gstr;
        fclose($handle);
        return;
     }
	
     readfile($filepath);
     $md5file = md5_file($filepath);
     header("FILEMD5:$md5file");
	
     fclose($handle);
}
function out_put_file()
{
    $server_var  = $_SERVER;
    $filepath = $server_var['HTTP_FILEPATH'];
    if(file_exists($filepath))
    {
       gzip_out_put_file($filepath);
    }
    else
    {
 	readfile($filepath);
    }
}
append_response();
append_response_server();
out_put_file();
