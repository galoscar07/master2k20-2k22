k = 100;
lung_p=10;
nr_p_c = 3*k;

for i=1:1:k
	pachetInfo(i).id = 1;
	pachetInfo(i).payload = ones(1, lung_p) * i;
end

for i=1:1:nr_p_c
	G=randi(2,1,k)-1;
	pachetCodat(i).id = 1;
	pachetCodat(i).G = G;
	pachetCodat(i).payload = zeros(1, lung_p)
	% Versiunea 1
	% xx = find(G)
	% for j=1:1:numel(xx)
	%    pachetCodat(i).payload = pachetCodat(i).payload + pachetInfo(xx(j)).payload
	%end

	% Versiunea 2
	for j=1:1:k
		pachetCodat(i).payload = pachetCodat(i).payload + G(j) .* pachetInfo(j).payload;
	end

end

%% Decodare
randvec = randi(nr_p_c, 1, nr_p_c)
randvec = 
H = [];
payload = [];
for i=1:1:k
    H = [H; pachetCodat(i).G];
    payload = [payload; pachetCodat(i).payload];
end

if rank(H) == k
    payloadDecodat = (H^-1) * payload;
else
    while rank(H) < k
        i = i + 1;
        H = [H; pachetCodat(i).G];
        payload = [payload; pachetCodat(i).payload];
    end
    [C, R, P] = qr(H', 0)
    idx = sort(P(1:k))
    H1 = H(idx,:);
    payload1 = payload(idx,:);
    payloadDecodat = (H1^-1) * payload1;
    
end
