% v1 = randsample(1:1000,1);
% v2 = randsample(1:10,1);
% v3 = randsample([1,5,10],1);
%  
% % Data for entropy
% abc = [];disc=[];
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% for ii = 1:6
%     mu = [0 0;0.0001 0.0001;0.001 0.001;0.01 0.01;0.1 0.1;...
%           1 1;1.5 1.5;2 2;2.5 2.5;3 3];
%     vb = {};
%     for i = 1:10
%         v = mu(i,:);
%         sigma = [v(1)+v(1)/4 v(1)+v(1)/4;v(1)+v(1)/4 v(1)+v(1)/4];
%         rng default
%         vb{i} = mvnrnd(v,sigma,10000);
%     end
% 
%     %for the normal, 
%     acc_normal=[];ini_po = [0,0];
%     for j = 1:39600
%         cd = vb{randsample(1:10,1)};
%         cd1  = cd(randsample(1:10000,1),:);
%         ini_po = cd1+ini_po;
%         acc_normal = vertcat(acc_normal,cd1+ini_po);
%     end
% 
% 
%     %for the sick
%     acc_sick=[];ini_po = [0,0];
%      for j = 1:39600
%         cd = vb{randsample([1,5,10],1)};
%         cd1  = cd(randsample(1:10000,1),:); 
%         ini_po = cd1+ini_po;
%         acc_sick = vertcat(acc_sick,ini_po);
%      end
% 
%      dist1 = diff(acc_normal);dist1 = sqrt(dist1(:,1).^2 + dist1(:,2).^2);
%      dist2 = diff(acc_sick);dist2 = sqrt(dist2(:,1).^2 + dist2(:,2).^2);
%      disc = horzcat(disc,dist1,dist2);
%      alldist = [dist1;dist2];
%      alldist = sort(alldist);
% 
% 
%      dd = length(alldist);ab = [];h = 5;df = 5;
%      while df>0
%        df =  mean(alldist(1:dd));
%        ab = vertcat(ab,df);
%        dd = numel(find(alldist<=df));
% 
%      end
% 
%  abc = horzcat(abc,ab);
%  
% end
%  
% % 
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % 
% % 
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % 
% % 
% % 
% % 
% % 
% % 
% % %Data for Kolmogorov complexity
% % 
% mu = [0.0001 0.0001;0.001 0.001;0.01 0.01;0.1 0.1;...
%       1 1;1.5 1.5;2 2;2.5 2.5;3 3;3.5 3.5];
% mu = mu*10;
% 
% vb = {};
% for i = 1:10
%     v = mu(i,:);
%     sigma = [v(1)+v(1)/4 v(1)+v(1)/4;v(1)+v(1)/4 v(1)+v(1)/4];
%     rng default
%     vb{i} = mvnrnd(v,sigma,10000);
% end
% 
% 
% 
% 
% kc_year = [];lodo = [];ca=[];ini_po=[0,0];
% 
% %representative of movement for one year.
% for j = 1:10  
%     for m = 1:5
%        for i = 1:8760
%            cd = vb{j};
%            cd1  = cd(randsample(1:10000,1),:);
%            ini_po = ini_po + cd1; 
%            ca = vertcat(ca,ini_po);  
%            
%        end
%        lodo = horzcat(lodo,ca);ca=[];ini_po=[0,0];
%     end
%    kc_year = horzcat(kc_year,lodo);
%    lodo=[];
% end
%  
% % representative of movement for one month.
% kc_month = [];lodo = [];ca=[];ini_po=[0,0];
% 
% for j = 1:10  
%     for m = 1:5
%        for i = 1:720
%            cd = vb{j};
%            cd1  = cd(randsample(1:10000,1),:);
%            ini_po = ini_po + cd1; 
%            ca = vertcat(ca,ini_po);  
%            
%        end
%        lodo = horzcat(lodo,ca);ca=[];ini_po=[0,0];
%     end
%    kc_month = horzcat(kc_month,lodo);
%    lodo=[];
% end
% 
% 
% gf = 0:2:size(kc_year,2);kcyear_dist=[];
% for j = 1:length(gf)-1
%     dg = (gf(j)+1:gf(j+1));
%     dg1 = kc_year(:,dg);
%     dg1 = diff(dg1);
%     dg2 = sqrt(dg1(:,1).^2+dg1(:,2).^2);
%     kcyear_dist = horzcat(kcyear_dist,dg2);
% end
% 
% gf = 0:2:size(kc_month,2);kcm_dist=[];
% for j = 1:length(gf)-1
%     dg = (gf(j)+1:gf(j+1));
%     dg1 = kc_month(:,dg);
%     dg1 = diff(dg1);
%     dg2 = sqrt(dg1(:,1).^2+dg1(:,2).^2);
%     kcm_dist = horzcat(kcm_dist,dg2);
% end




% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% synthetic data for outlier detection.

mu = [0 0;0.0001 0.0001;0.001 0.001;0.01 0.01;0.1 0.1;...
      1 1;1.5 1.5;2 2;2.5 2.5;3 3];
%rng default


 vb = {};ini_po=[0,0];
for i = 1:10
    v = mu(i,:);
    sigma = [v(1)/4 v(1)/4;v(1)/4 v(1)/4];
    
    vb{i} = mvnrnd(v,sigma,10000);
    
end




out_data={};
wb = [0.25,0.5,0.75,1];allofme={};

id = [];traj = [];id_u=[];id_me={};
for t = 1:length(wb)
  for m = 1:66
          
     u = randsample(1:5,1);% selects the no of agents with abnormal movement.
     id = vertcat(id,11-u,u);
     cd = randsample(1:11,u);%selects the id of the agents with abnormal movement.
     nncd = setdiff(1:11,cd);% gets the id of the normal ones
    
     abn_time = wb(1)*600; good_time = 600-abn_time;%computes the proportion of time for normal and abnormal movements.
          
        
     ghno = randsample(1:10,1);%selects the data bin for normal agents
     jk = setdiff(1:10,ghno);%computes the remaining bin available for selection
     ghno = vb{ghno};%selects the data bin for normal agents
     ghan = vb{randsample(jk,1)};%selects the data bin for abnormal different from normal;
     
     tapo = [];%tapo1 = zeros(1,length(nncd)*2);
     tapo1=[];
     
     for k = 1:length(nncd)%for normal
         da = ghno(randsample(1:10000,600),:);
         tapo = horzcat(tapo,da);
     end
     
     tapo1 = vertcat(tapo1,tapo);  
     tapo1 = cumsum(tapo1);
     traj = horzcat(traj,tapo1);
     tapo = [];
     
     
     tapo = [];%tapo1 = zeros(1,length(cd)*2);
     tapo1=[];
     
     for k = 1:length(cd)%for abnormal
         da = ghan(randsample(1:10000,abn_time),:);
         da = vertcat(da,ghno(randsample(1:10000,good_time),:));
         tapo = horzcat(tapo,da);
     end
     
     tapo1 = vertcat(tapo1,tapo);
     tapo1 = cumsum(tapo1);
     traj = horzcat(traj,tapo1);
     tapo = [];tapo1=[];
     
     %traj = vertcat(traj,id);
     out_data{m} = traj;id_u = horzcat(id_u,id);id=[];traj=[];
  end
   allofme{t} = out_data;out_data = {};id_me{t} = id_u;id_u=[];
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

allof_dist = {};gf = 0:2:22;nv = [];nm=[];
for i = 1:4
    gp = allofme{1,i};
    for j = 1:size(gp,2)
        gp1 = gp{1,j};
        for ii = 1:length(gf)-1
            yr = gp1(:,gf(ii)+1:gf(ii+1));
            yr1 = sum(sqrt(yr(:,1).^2+yr(:,2).^2));
            nv = horzcat(nv,yr1);          
        end
        nm= horzcat(nm,nv');nv=[];
    end
    allof_dist{i} =nm;nm=[];
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
t1=[];t2=[];t3=[];t4=[];global rrr;out_acc={};rrr=[];global gv;global m3;global uuu;
fp={};
for tt = 1:4
    gk = allof_dist{1,tt};gv = id_me{1,tt};gv = gv(2,:);
    m3 = gk;
    outlier_algo;
    out_acc{tt} = rrr;rrr=[];
    fp{tt} = uuu;uuu=[];%false positives
    
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%evaluate algorithms based on the temporal duration of abnormal movement.

%(1)


vb = [];
for i = 1:length(out_acc)
    vb = horzcat(vb, mean(out_acc{1,i},2));
    
end


%confidence interval for accuraccy temporal
cf=[];cf1=[];
for i = 1:4   
   xx = out_acc{1,i};
   for j = 1:size(xx,1)
       x = xx(j,:);
      SEM = std(x)/sqrt(length(x));               % Standard Error
      ts = tinv([0.025  0.975],length(x)-1);      % T-Score
      CI = mean(x) + ts*SEM;   
      cf1 = vertcat(cf1,CI);
   end    % Confidence Intervals
   cf = vertcat(cf,cf1);cf1=[];
end





%(2)


% mean values of false positives temporal
vb1 = [];fp1={};
for i = 1:length(fp)
    cn = fp{1,i};cn(find(isnan(cn)))= 0;fp1{i}=cn;
    vb1 = horzcat(vb1, mean(cn,2));
    
end
%confidence interval for false positives temporal
cff=[];cf1=[];
for i = 1:4   
   xx = fp1{1,i};
   for j = 1:size(xx,1)
       x = xx(j,:);
      SEM = std(x)/sqrt(length(x));               % Standard Error
      ts = tinv([0.025  0.975],length(x)-1);      % T-Score
      CI = mean(x) + ts*SEM;   
      cf1 = vertcat(cf1,CI);
   end    % Confidence Intervals
   cff = vertcat(cff,cf1);cf1=[];
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%evaluate algorithms based on the number agents with outliers across each
%time window

%(3)
c1=[];c2=[];c3=[];c4=[];c5=[];
cj = cell(1,5);cj{1,5} = [];

for i = 1:length(out_acc)
    gv = id_me{1,tt};gv = gv(2,:);
    gv1 = out_acc{1,i};
    
    for j = 1:length(gv)
        if gv(j)==1
            cj{1} = horzcat(cj{1},gv1(:,j));
        elseif gv(j)==2
             cj{2} = horzcat(cj{2},gv1(:,j));
             
        elseif gv(j)==3
             cj{3} = horzcat(cj{3},gv1(:,j));
             
        elseif gv(j)==4
            
            cj{4} = horzcat(cj{4},gv1(:,j));
        else 
            
            cj{5} = horzcat(cj{5},gv1(:,j));
        end
        
    end
    
    
end

% mean values of  no of agents with outliers
vb12 = [];
for i = 1:length(cj)
    vb12 = horzcat(vb12, mean(cj{1,i},2));
    
end

bnx=[];cf1=[];
for j = 1:length(cj)
    x = cj{1,j};
    for i = 1:size(x,1)
        vn = x(i,:);
        SEM = std(vn)/sqrt(length(vn)); 
        ts = tinv([0.025  0.975],length(vn)-1); 
        c1x = mean(vn) + ts*SEM;
        cf1 = vertcat(cf1,c1x);
        
    end
    bnx = vertcat(bnx,cf1);cf1=[];
end
  


%(4)

%evaluate algorithms based on the number agents with outliers across each
%time window false positives
cjx = cell(1,5);cjx{1,5} = [];

for i = 1:length(out_acc)
    gv = id_me{1,tt};gv = gv(2,:);
    gv1 = fp1{1,i};
    
    for j = 1:length(gv)
        if gv(j)==1
            cjx{1} = horzcat(cjx{1},gv1(:,j));
        elseif gv(j)==2
             cjx{2} = horzcat(cjx{2},gv1(:,j));
             
        elseif  gv(j)==3
             cjx{3} = horzcat(cjx{3},gv1(:,j));
             
        elseif gv(j)==4
            
            cjx{4} = horzcat(cjx{4},gv1(:,j));
        else 
            
            cjx{5} = horzcat(cjx{5},gv1(:,j));
        end
        
    end
    
    
end

% mean values of  no of agents with outliers falsepositives
vb22 = [];
for i = 1:length(cj)
    vb22 = horzcat(vb22, mean(cjx{1,i},2));
    
end



bnxfp=[];cf1=[];
for j = 1:length(cjx)
    x = cjx{1,j};
    for i = 1:size(x,1)
        vn = x(i,:);
        SEM = std(vn)/sqrt(length(vn)); 
        ts = tinv([0.025  0.975],length(vn)-1); 
        c1x = mean(vn) + ts*SEM;
        cf1 = vertcat(cf1,c1x);
        
    end
    bnxfp = vertcat(bnxfp,cf1);cf1=[];
end
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%





