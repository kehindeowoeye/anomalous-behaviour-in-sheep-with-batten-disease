%script for the first plot in the paper, note that i used the data fro, 3600 onwards after extracting the relevant data with
%the code below



A = []; 
A_time = []; 
for i = 1:length(LSG)
   x = trajectory_matrix(1:2,1:length(obs_indicator),i); 
   x1 = x'; 
   c = LSG(:,1);c1 = c(i); c2 = repmat(c1,1,length(obs_indicator));c2 = c2'; 
   d = LSG(:,2);d1 = d(i); d2 = repmat(d1,1,length(obs_indicator));d2 = d2'; 
   e = LSG(:,3);e1 = e(i); e2 = repmat(e1,1,length(obs_indicator));e2 = e2'; 
   f = LSG(:,4);f1 = f(i); f2 = repmat(f1,1,length(obs_indicator));f2 = f2'; 
   g = LSG(:,5);g1 = g(i); g2 = repmat(g1,1,length(obs_indicator));g2 = g2'; 
   h = LSG(:,6);h1 = h(i); h2 = repmat(h1,1,length(obs_indicator));h2 = h2'; 
   k = LSG(:,7);k1 = k(i); k2 = repmat(k1,1,length(obs_indicator));k2 = k2'; 
   t1 = datetime(time_matrix(1,:)); 
   t2 = datetime(time_matrix(2,:)); 
   t =  t1:hours(1/3600):t2; 
   B = horzcat(x1,c2,d2,e2,f2,g2,h2,k2); 
   A = vertcat(A,B); 
   A_time = vertcat(A_time,t); 
   B = []; 
end 

A1 = (reshape(A_time',1,[]))'; 
A = horzcat(A, datevec(A1)); 
A2 = find(A1==datetime([2011,03,22,11,00,00])); 

AK = []; 
AA = []; 
for i = 1:length(A2) 
    for j = A2(i):A2(i)+56000
        AK = vertcat(AK,A(j,1:15)); 
    end 
    AA = vertcat(AA,AK); 
    AK = []; 
end 



 
 


m = []; 
m1 = []; 
a1 = 0:56001:length(AA); 
a1 = a1(1:length(a1)); 
%a1 = 0:84660:length(AA); 
%a1 = a1(2:length(a1)); 
a2 = 2; 

  c1 = AA(:,1);c2 = AA(:,2);
Ax=[];Ay=[];
for b = 2:length(LSG)+1
    cx = c1((a1(b-1)+1 :a1(b)),:);cy = c2((a1(b-1)+1 :a1(b)),:);
    Ax = horzcat(Ax,cx);Ay = horzcat(Ay,cy);
end


lapa = 1:600:67800;
Ax1 = Ax(lapa',:);Ay1 = Ay(lapa',:);

mada = LSG;
ag = (find(mada(:,3)==2009));
mada = mada(ag,:);



acc={};
for i = 1:11
    rx = Ax1(:,ag(i))- Ax1;ry = Ay1(:,ag(i))-Ay1;
    acc{i} =  sqrt(rx.^2 + ry.^2);
end

acc1={};po=[];
for i = 1:11
    bu = acc{i};
    for j = 1:size(bu,1)
        po = vertcat(po, sort(bu(j,:)));
        
    end
    acc1{i}=po;po=[];
end

acc2={};po1=[]; copo=[];
for i = 1:11
    la = acc1{i};ap = acc{i};
    for j =  1:size(bu,1)
        la1 = la(j,:);ap1 = ap(j,:);
        for k = 1:length(la1)
            cd = find(ap1==la1(k));  
            copo = horzcat(copo,cd);
        end
        po1 = vertcat(po1,copo);copo=[];
    end
    acc2{i}=po1;po1=[];
end

guu = [];
for i = 1:11
    guu = vertcat(guu,acc2{i});
end

nn = []; 
for j = 1:length(a1)
    %B = a1(j)+1:a1(j+1); 
    for i = a2:a1(j)
      lat1 = AA(i-1,1);lat2 = AA(i,1);lon1 = AA(i-1,2);lon2 = AA(i,2); 
      m_dist = sqrt((lat2-lat1)^2 + (lon2-lon1)^2); 
      m = vertcat(m,m_dist); 
    end 
    m1 = horzcat(m1,m); 
    m = []; 
    a2 = a1(j)+2; 
    nn = horzcat(nn,a1(j)); 
end 

m1 = m1(3600:end,:);m1 = m1(1:76200,:);

% %Cut trajectory into parts 
% 
m3 = []; m1 = m1(1:55800,:);
b2 = size(m1); 
for i = 1:b2(2) 
    M=sum(reshape(m1(:,i),600,[])); 
    m3 = vertcat(m3,M); 
end 
nnb = size(m3); 
m31 = m3(:); 
da = m3;



% b = LSG(:,5);b5 = find(b==5);b6 = find(b==6);Ax1 =[];Ay1=[];
% c=[];
% %c = vertcat(c,b5,b6);
% %c = [9 2 7 6 11 8 10 1 3 4 5];
% c = [2 10 8 7 9 5 1 6 4 3 11];
% for y = 1:11
%     Ax1 = horzcat(Ax1,Ax(:,c(y)));
%     Ay1 = horzcat(Ay1,Ay(:,c(y)));
% end


%Ax = Ax(3601:3601+59999,:);
%Ay = Ay(3601:3601+59999,:);
