function [answer] = matrix_pencil(x,p,Ts)

N=length(x);
Y=hankel(x(1:end-p),x(end-p:end));

Y1=Y(:,1:end-1);
Y2=Y(:,2:end);

l=eig(pinv(Y1)*Y2);

alfa=log(abs(l))/Ts;
freq=atan2(imag(l),real(l))/(2*pi*Ts);

Z=zeros(N,p);
for i = 1:length(l)
Z(:,i)=transpose(l(i).^(0:N-1));
end

rZ=real(Z);
iZ=imag(Z);

rZ(isinf(rZ))=realmax*sign(rZ(isinf(rZ)));
iZ(isinf(iZ))=realmax*sign(iZ(isinf(iZ)));

Z=rZ+1i*iZ;
h=Z\x;
Amp=abs(h);
theta=atan2(imag(h),real(h));

answer=[Amp theta alfa freq];

end

