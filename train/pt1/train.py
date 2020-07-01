import os
import traceback

import torch
import torch.nn.functional as F
import torch.optim as optim
from dataset import ColorDataset
import numpy as np
from torch.utils.data import DataLoader
from colornet import ColorNet
import textdistance
import hashlib

torch.cuda.set_device(2)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

train_set = ColorDataset('train')
train_loader = torch.utils.data.DataLoader(train_set, batch_size=20, shuffle=True, num_workers=4)
color_model = ColorNet()
# if os.path.exists('/home/wsf/colornet_params.pkl'):
#    color_model.load_state_dict(torch.load('/home/wsf/colornet_params.pkl'))
color_model.to(device)

learning_rate = 1.2e-4
optimizer = optim.AdamW(color_model.parameters(), amsgrad=True, lr=learning_rate)
criterion = torch.nn.CrossEntropyLoss()


def train():
    try:
        for epoch in range(21):
            print("Epoch: %d" % epoch)
            for batch_idx, (data, label) in enumerate(train_loader):
                messagefile = open('/out/logs/message.txt', 'a')
                img_gray, img_ab = data
                img_gray = img_gray.to(device)
                img_ab = img_ab.to(device)
                label = label.to(device).type(torch.long)

                color_model.train()
                optimizer.zero_grad()

                class_output, output = color_model(img_gray, img_gray)
                ems_loss = torch.pow((img_ab - output), 2).sum() / torch.from_numpy(
                    np.array(list(output.size()))).prod()
                cross_entropy_loss = 1 / 350 * criterion(class_output, label)
                loss = ems_loss + cross_entropy_loss

                lossmsg = 'loss: %.9f\n' % (loss.item())
                messagefile.write(lossmsg)
                loss.backward()
                optimizer.step()

                if batch_idx % 500 == 0:
                    message = 'Train Epoch:%d\tPercent:[%d/%d (%.0f%%)]\tLoss:%.9f\n' % (
                        epoch, batch_idx * len(data), len(train_loader.dataset),
                        100. * batch_idx / len(train_loader), loss.item())
                    print(message)
                    messagefile.write(message)
                    torch.save(color_model.state_dict(), '/out/colornet_params.pkl')
            torch.save(color_model.state_dict(), '/out/colornet_params_ep_%s.pkl' % epoch)
    except Exception:
        print(traceback.format_exc())
    finally:
        torch.save(color_model.state_dict(), '/out/colornet_params_wtf.pkl')


if __name__ == '__main__':
    print("Alternative Training Mode, lr: %f" % learning_rate)
    print(torch.__version__)
    if torch.cuda.is_available():
        print("Using CUDA")
    train()
