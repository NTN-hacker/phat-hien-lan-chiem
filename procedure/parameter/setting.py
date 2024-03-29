
Parameter = {
    #DBP
    "587c79e9b807da0011e33d3d" :  {
        "name": "CAM_DBP",

        "time-update": 12.5,

        "url": "curl \"http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id=587c79e9b807da0011e33d3d&bg=black\"  -H \"Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4\"   -H \"Cache-Control: no-cache\"   -H \"Connection: keep-alive\"  -H \"Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4\"   -H \"Cache-Control: no-cache\"   -H \"Connection: keep-alive\" -H \"Cookie: GUEST_LANGUAGE_ID=vi_VN; _ga=GA1.3.1268639869.1637042764; ASP.NET_SessionId=whhmth0edrixbfoydshhg321; .VDMS=2CF9AF29877107034C56C9D51CBEAE47FD899DED662CFBB5CBCEC7A62F97DB60F5C8FE341A12F6AD3E69E32B9546499219D77B0A76197BD52BF5F71C799B7F95E1A68A7D5A94399BE5C38D66786A8983ECBD5FB32FC51D47CE7DCF103EE11B65EDACE38441D20196BAAA45CC40CC32998E1D7AE4; _frontend=\u0021nw6dooWn8pGIKqFmil1P2lbeEwNhYVww9WP2z4x6h9kTylkUspJirO5K6GJzkWZkAtNCeYsAB3gpIT8=; CurrentLanguage=vi; _gid=GA1.3.446387129.1652343216; _pk_ref.1.2f14=%5B%22%22%2C%22%22%2C1652343216%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.2f14=a912fbe1c12c6e6e.1652249178.2.1652343264.1652343216.\" -H \"Pragma: no-cache\"   -H \"Upgrade-Insecure-Requests: 1\"   -H \"User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\"--compressed   --insecure --output test/CAM_DBP/root/img_test\" ",
        
        "threahold": {
            "lower_thread" : [8, 100, 50],
            "upper_thread" : [180, 255, 255],
            "area" : 300,
            "width": 30,
            "height": 30,
            "percentage": 10
        },
        "roi" : [[296, 135, 146, 155], [292, 135, 156, 156]],
        'lst_roi' : {
            '1':  [[0, 0], [0, 4], [1, 200], [70, 193]],
            '2': [[60, 0], [220, 0], [220, 200], [175, 200]]
        }
        
    },
    #TOKY
     "589ad89eb3bf7600110283ac" :  {
        "name" : "CAM_TOKY",

        "time-update": 12.5,

		"url":"curl 'http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id=589ad89eb3bf7600110283ac&bg=black'   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'   -H 'Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4'   -H 'Cache-Control: no-cache'   -H 'Connection: keep-alive'   -H $'Cookie: GUEST_LANGUAGE_ID=vi_VN; _ga=GA1.3.1268639869.1637042764; ASP.NET_SessionId=whhmth0edrixbfoydshhg321; .VDMS=2CF9AF29877107034C56C9D51CBEAE47FD899DED662CFBB5CBCEC7A62F97DB60F5C8FE341A12F6AD3E69E32B9546499219D77B0A76197BD52BF5F71C799B7F95E1A68A7D5A94399BE5C38D66786A8983ECBD5FB32FC51D47CE7DCF103EE11B65EDACE38441D20196BAAA45CC40CC32998E1D7AE4; _frontend=\u0021nw6dooWn8pGIKqFmil1P2lbeEwNhYVww9WP2z4x6h9kTylkUspJirO5K6GJzkWZkAtNCeYsAB3gpIT8=; CurrentLanguage=vi; _pk_ref.1.2f14=%5B%22%22%2C%22%22%2C1652343216%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.2f14=a912fbe1c12c6e6e.1652249178.2.1652343264.1652343216.'   -H 'Pragma: no-cache'   -H 'Upgrade-Insecure-Requests: 1'   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'   --compressed   --insecure",
        
        "threahold": {
            "lower_thread" : [8, 100, 50],
            "upper_thread" : [180, 255, 255],
            "area" : 150,
            "width": 30,
            "height": 30,
            "percentage": 10
        },
        "roi" : [[416, 100, 470, 170], [416, 100, 470, 170]], 
        'lst_roi' : {
            '1':  [[0, 60], [0, 70], [0, 185],  [195, 185]],
            '2':  [[[0, 0], [0, 0],  [195, 0], [195, 40]]]
        }  
   },
   #VL_NTT
   "5ad06a0d98d8fc001102e27b": {
    "name" : "CAM_VL_NTT",

        "time-update": 12.5,

		"url":"curl 'http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id=5ad06a0d98d8fc001102e27b&bg=black'   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'   -H 'Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4'   -H 'Cache-Control: no-cache'   -H 'Connection: keep-alive'   -H $'Cookie: GUEST_LANGUAGE_ID=vi_VN; _ga=GA1.3.1268639869.1637042764; ASP.NET_SessionId=whhmth0edrixbfoydshhg321; .VDMS=2CF9AF29877107034C56C9D51CBEAE47FD899DED662CFBB5CBCEC7A62F97DB60F5C8FE341A12F6AD3E69E32B9546499219D77B0A76197BD52BF5F71C799B7F95E1A68A7D5A94399BE5C38D66786A8983ECBD5FB32FC51D47CE7DCF103EE11B65EDACE38441D20196BAAA45CC40CC32998E1D7AE4; _frontend=\u0021nw6dooWn8pGIKqFmil1P2lbeEwNhYVww9WP2z4x6h9kTylkUspJirO5K6GJzkWZkAtNCeYsAB3gpIT8=; CurrentLanguage=vi; _pk_ref.1.2f14=%5B%22%22%2C%22%22%2C1652343216%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.2f14=a912fbe1c12c6e6e.1652249178.2.1652343264.1652343216.'   -H 'Pragma: no-cache'   -H 'Upgrade-Insecure-Requests: 1'   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'   --compressed   --insecure",
        
        "threahold": {
            "lower_thread" : [8, 100, 50],
            "upper_thread" : [180, 255, 255],
            "area" : 150,
            "width": 30,
            "height": 30,
            "percentage": 10
        },
        "roi" : [[287, 98, 500, 291], [287, 98, 500, 291]], 
        'lst_roi' : {
            '1':  [[0, 0], [0, 0], [0, 195],  [166, 195]],
            '2':  [[20, 0], [230, 0],  [230, 195], [230, 195]]
        }
   },
   #SG
   "5f000ab3942cda00169ee00b": {
    "name" : "CAM_SGTVT",

    "time-update": 12.5,

    "url":"curl 'http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id=5f000ab3942cda00169ee00b&bg=black'   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'   -H 'Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4'   -H 'Cache-Control: no-cache'   -H 'Connection: keep-alive'   -H $'Cookie: GUEST_LANGUAGE_ID=vi_VN; _ga=GA1.3.1268639869.1637042764; ASP.NET_SessionId=whhmth0edrixbfoydshhg321; .VDMS=2CF9AF29877107034C56C9D51CBEAE47FD899DED662CFBB5CBCEC7A62F97DB60F5C8FE341A12F6AD3E69E32B9546499219D77B0A76197BD52BF5F71C799B7F95E1A68A7D5A94399BE5C38D66786A8983ECBD5FB32FC51D47CE7DCF103EE11B65EDACE38441D20196BAAA45CC40CC32998E1D7AE4; _frontend=\u0021nw6dooWn8pGIKqFmil1P2lbeEwNhYVww9WP2z4x6h9kTylkUspJirO5K6GJzkWZkAtNCeYsAB3gpIT8=; CurrentLanguage=vi; _pk_ref.1.2f14=%5B%22%22%2C%22%22%2C1652343216%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.2f14=a912fbe1c12c6e6e.1652249178.2.1652343264.1652343216.'   -H 'Pragma: no-cache'   -H 'Upgrade-Insecure-Requests: 1'   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'   --compressed   --insecure",
    
    "threahold": {
        "lower_thread" : [8, 100, 50],
        "upper_thread" : [180, 255, 255],
        "area" : 150,
        "width": 30,
        "height": 30,
        "percentage": 10
    },
    "roi" : [[390, 180, 490, 287], [390, 180, 490, 287]], 
    'lst_roi' : {
        '1':  [[89, 0],  [150, 122], [190, 0], [190, 131]],
        '2':  [[89, 0],  [150, 122], [190, 0], [190, 131]]
    }
   },
   #DTH_VTS
  
     "5a8241105058170011f6eaa6": {
    "name" : "CAM_DTH_VTS",

    "time-update": 12.5,

    "url":"curl 'http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id=5a8241105058170011f6eaa6&bg=black'   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'   -H 'Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4'   -H 'Cache-Control: no-cache'   -H 'Connection: keep-alive'   -H $'Cookie: GUEST_LANGUAGE_ID=vi_VN; _ga=GA1.3.1268639869.1637042764; ASP.NET_SessionId=whhmth0edrixbfoydshhg321; .VDMS=2CF9AF29877107034C56C9D51CBEAE47FD899DED662CFBB5CBCEC7A62F97DB60F5C8FE341A12F6AD3E69E32B9546499219D77B0A76197BD52BF5F71C799B7F95E1A68A7D5A94399BE5C38D66786A8983ECBD5FB32FC51D47CE7DCF103EE11B65EDACE38441D20196BAAA45CC40CC32998E1D7AE4; _frontend=\u0021nw6dooWn8pGIKqFmil1P2lbeEwNhYVww9WP2z4x6h9kTylkUspJirO5K6GJzkWZkAtNCeYsAB3gpIT8=; CurrentLanguage=vi; _pk_ref.1.2f14=%5B%22%22%2C%22%22%2C1652343216%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.2f14=a912fbe1c12c6e6e.1652249178.2.1652343264.1652343216.'   -H 'Pragma: no-cache'   -H 'Upgrade-Insecure-Requests: 1'   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'   --compressed   --insecure",
    
    "threahold": {
        "lower_thread" : [8, 100, 50],
        "upper_thread" : [180, 255, 255],
        "area" : 150,
        "width": 30,
        "height": 30,
        "percentage": 10
    },
    "roi" : [[260, 80, 514, 289], [260, 80, 514, 289]], 
    'lst_roi' : {
        '1':  [[0, 39], [0, 39], [0, 185], [195, 185]],
        '2':  [[0, 0], [0, 0], [195, 0], [195, 84]]
    }
   }
}



  
  
 